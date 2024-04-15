def get_args():
    if not getattr(get_args, 'data', False):
        import torch
        from argparse import ArgumentParser

        parser = ArgumentParser()  # noqa
        parser.add_argument('--driven_audio', default='./examples/driven_audio/bus_chinese.wav', help='path to driven audio')
        parser.add_argument('--source_image', default='./examples/source_image/full_body_1.png', help='path to source image')
        parser.add_argument('--ref_eyeblink', default=None, help='path to reference video providing eye blinking')
        parser.add_argument('--ref_pose', default=None, help='path to reference video providing pose')
        parser.add_argument('--checkpoint_dir', default='./checkpoints', help='path to output')
        parser.add_argument('--result_dir', default='./results', help='path to output')
        parser.add_argument('--pose_style', type=int, default=0, help='input pose style from [0, 46)')
        parser.add_argument('--batch_size', type=int, default=2, help='the batch size of facerender')
        parser.add_argument('--size', type=int, default=256, help='the image size of the facerender')
        parser.add_argument('--expression_scale', type=float, default=1., help='the batch size of facerender')
        parser.add_argument('--input_yaw', nargs='+', type=int, default=None, help='the input yaw degree of the user ')
        parser.add_argument('--input_pitch', nargs='+', type=int, default=None, help='the input pitch degree of the user')
        parser.add_argument('--input_roll', nargs='+', type=int, default=None, help='the input roll degree of the user')
        parser.add_argument('--enhancer', type=str, default=None, help='Face enhancer, [gfpgan, RestoreFormer]')
        parser.add_argument('--background_enhancer', type=str, default=None, help='background enhancer, [realesrgan]')
        parser.add_argument('--cpu', dest='cpu', action='store_true')
        parser.add_argument('--face3dvis', action='store_true', help='generate 3d face and 3d landmarks')
        parser.add_argument('--still', action='store_true', help='can crop back to the original videos for the full body aniamtion')
        parser.add_argument('--preprocess', default='crop', choices=['crop', 'extcrop', 'resize', 'full', 'extfull'], help='how to preprocess the images')
        parser.add_argument('--verbose', action='store_true', help='saving the intermedia output or not')
        parser.add_argument('--old_version', action='store_true', help='use the pth other than safetensor version')

        # net structure and parameters
        parser.add_argument('--net_recon', type=str, default='resnet50', choices=['resnet18', 'resnet34', 'resnet50'], help='useless')
        parser.add_argument('--init_path', type=str, default=None, help='Useless')
        parser.add_argument('--use_last_fc', default=False, help='zero initialize the last fc')
        parser.add_argument('--bfm_folder', type=str, default='./checkpoints/BFM_Fitting/')
        parser.add_argument('--bfm_model', type=str, default='BFM_model_front.mat', help='bfm model')

        # default renderer parameters
        parser.add_argument('--focal', type=float, default=1015.)
        parser.add_argument('--center', type=float, default=112.)
        parser.add_argument('--camera_d', type=float, default=10.)
        parser.add_argument('--z_near', type=float, default=5.)
        parser.add_argument('--z_far', type=float, default=15.)

        args = parser.parse_args()
        args.device = 'cuda' if torch.cuda.is_available() and not args.cpu else 'cpu'
        get_args.args = args

    return get_args.args


def models():
    if not getattr(models, 'data', False):
        import shutil
        import torch
        from time import strftime
        import os
        import sys

        from src.utils.preprocess import CropAndExtract
        from src.test_audio2coeff import Audio2Coeff
        from src.facerender.animate import AnimateFromCoeff
        from src.generate_batch import get_data
        from src.generate_facerender_batch import get_facerender_data
        from src.utils.init_path import init_path

        args = get_args()

        # === Init paths
        current_root_path = os.path.split(sys.argv[0])[0]
        sadtalker_paths = init_path(
            args.checkpoint_dir,
            os.path.join(current_root_path, 'src/config'),
            args.size,
            args.old_version,
            args.preprocess,
        )

        # === Initialize models
        preprocess_model = CropAndExtract(sadtalker_paths, args.device)
        audio_to_coeff = Audio2Coeff(sadtalker_paths, args.device)
        animate_from_coeff = AnimateFromCoeff(sadtalker_paths, args.device)
        models.models = preprocess_model, audio_to_coeff, animate_from_coeff

    return models.models
