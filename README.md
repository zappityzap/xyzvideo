![xyzvideo logo](logo.jpg)

[Examples](#examples) | [Install](#install) | [Usage](#usage)

XYZ Plot for video outputs in Automatic1111, forked from the official XYZ Plot in version 1.7.0.

Designed to work with [sd-webui-animatediff](https://github.com/continue-revolution/sd-webui-animatediff)
* Inputs: GIF, MP4, WebM
* Output: MP4

# Examples
Steps (10, 30, 50)
[![Steps](https://zappityzap.github.io/xyzvideo/assets/images/001.jpg)](https://zappityzap.github.io/xyzvideo/assets/videos/xyz_grid-00001.mp4)

CFG (5, 7, 10)
[![CFG](https://zappityzap.github.io/xyzvideo/assets/images/002.jpg)](https://zappityzap.github.io/xyzvideo/assets/videos/xyz_grid-00002.mp4)

Motion modules (mm_sd15 v1, v2 v3)
[![Motion modules](https://zappityzap.github.io/xyzvideo/assets/images/003.jpg)](https://zappityzap.github.io/xyzvideo/assets/videos/xyz_grid-00003.mp4)

Samplers (Euler, DPM++ 2M Karras, DPM++ 2M SDE)
[![Samplers](https://zappityzap.github.io/xyzvideo/assets/images/009.jpg)](https://zappityzap.github.io/xyzvideo/assets/videos/xyz_grid-00009.mp4)

Checkpoints (Photon v10, ICBINP v10, zootvision v50)
[![Checkpoints](https://zappityzap.github.io/xyzvideo/assets/images/008.jpg)](https://zappityzap.github.io/xyzvideo/assets/videos/xyz_grid-00008.mp4)

# Install
Install from Git repo URL. Note that captions may require modifying the ImageMagick policy.xml to remove or comment out this line:
```
<!-- <policy domain="path" rights="none" pattern="@*" /> -->
```

# Usage
1. Enable AnimateDiff
1. Select MP4 output format in AnimateDiff
1. Select **X/Y/Z video plot** script from the Scripts dropdown list
1. Set X/Y/Z parameters
1. Generate
Outputs are stored in ```txt2img-grids```.

## Known Issues
PRs welcome!
* Doesn't if check AnimateDiff output format is set to MP4 before generating grid, so grid generation will fail after generating all the cells. Remember to set AnimateDiff output to MP4!
* Adding captions to video grid requires modifying ImageMagick configuration.
* Config Presets not working with img2img.
* Z-axis grids reuse the XY grid video, compressing the video an additional time.

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
