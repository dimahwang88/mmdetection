checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
dist_params = dict(backend='nccl')
log_level = 'INFO'
# load_from = '/home/dmitriy.khvan/mmdetection/checkpoints/coco_bepro_ckpt.pth'
load_from = '/home/dmitriy.khvan/mmdetection/checkpoint/crcnn_r50_bepro_origs.pth'
resume_from = None
workflow = [('train', 1), ('val', 1)]