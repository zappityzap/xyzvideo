![xyzvideo logo](logo.jpg)

[Install](#install) | [Usage](#usage) | [Examples](#examples)

XYZ Plot for video outputs in Automatic1111, forked from the official XYZ Plot in version 1.7.0.

Designed to work with [sd-webui-animatediff](https://github.com/continue-revolution/sd-webui-animatediff)
* Inputs: GIF, MP4, WebM
* Output: MP4

# Install
Install like any other extension. Note that captions may require modifying the ImageMagick policy.xml to remove or comment out this line:
```
<!-- <policy domain="path" rights="none" pattern="@*" /> -->
```

## Known Issues
* Captions require modifying ImageMagick configuration
* Config Presets not working with img2img
* Z-axis grids reuse the XY grids, compressing the video an additional time

## UI Compatibility
* Automatic1111: Yes, v1.7.0+

## Extension Compatibility
* [sd-webui-animatediff](https://github.com/continue-revolution/sd-webui-animatediff): Yes
* [Config Presets](https://github.com/Zyin055/Config-Presets): Yes, except for multi-select options like checkpoint or sampler.
<details>
    <summary>Custom fields for Config Presets</summary>

    # XYZ Video txt2img
    script_txt2img_xyz_video_plot_x_type
    script_txt2img_xyz_video_plot_y_type
    script_txt2img_xyz_video_plot_z_type
    script_txt2img_xyz_video_plot_x_values
    script_txt2img_xyz_video_plot_y_values
    script_txt2img_xyz_video_plot_z_values
    script_txt2img_xyz_video_plot_draw_caption
    script_txt2img_xyz_video_plot_no_fixed_seeds
    script_txt2img_xyz_video_plot_include_lone_videos
    script_txt2img_xyz_video_plot_include_sub_grids
    script_txt2img_xyz_video_plot_margin_size
    script_txt2img_xyz_video_plot_csv_mode

    # XYZ Video txt2img
    script_img2img_xyz_video_plot_x_type
    script_img2img_xyz_video_plot_y_type
    script_img2img_xyz_video_plot_z_type
    script_img2img_xyz_video_plot_x_values
    script_img2img_xyz_video_plot_y_values
    script_img2img_xyz_video_plot_z_values
    script_img2img_xyz_video_plot_draw_caption
    script_img2img_xyz_video_plot_no_fixed_seeds
    script_img2img_xyz_video_plot_include_lone_videos
    script_img2img_xyz_video_plot_include_sub_grids
    script_img2img_xyz_video_plot_margin_size
    script_img2img_xyz_video_plot_csv_mode
</details>

## Version History
* [v0.0.1](https://github.com/zappityzap/cyzvideo/releases/tag/v0.0.1) - First release

# Usage
1. Enable AnimateDiff
1. Select MP4 output format in AnimateDiff
1. Select **X/Y/Z video plot** script from the Scripts dropdown list
1. Set X/Y/Z parameters
1. Generate

# Examples
Motion modules
CFG
Steps
Samplers
Checkpoints
