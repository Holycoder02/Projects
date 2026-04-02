# Image Slideshow 🖼️

A beautiful GUI-based image slideshow viewer that automatically cycles through your favorite images with a configurable delay.

## Features

- 🖼️ **Multiple Image Support** - Load and display multiple images in sequence
- ⏸️ **Auto-Cycling** - Automatic image rotation every 3 seconds
- 📐 **Image Resizing** - All images automatically resized to 1080×1080 pixels
- 🎛️ **Start/Stop Control** - Button to control slideshow playback
- 🖥️ **GUI Interface** - Clean, user-friendly Tkinter-based window
- 🔄 **Infinite Loop** - Continuous cycling through images

## Requirements

- Python 3.6 or higher
- pillow (PIL) library for image handling
- tkinter (usually included with Python)

## Installation

### Step 1: Install Dependencies

```bash
pip install pillow
```

### Step 2: Navigate to Project Folder

```bash
cd "Image slide show"
```

### Step 3: Run the Application

```bash
python main.py
```

## Setup Instructions

### Adding Your Images

Edit the `main.py` file and locate the `image_paths` list. Add the full paths to your images:

```python
image_paths = [
    r"C:\Users\YourName\Pictures\image1.jpg",
    r"C:\Users\YourName\Pictures\image2.png",
    r"C:\Users\YourName\Pictures\image3.avif",
    # Add more paths here
]
```

**Important**: Use raw strings (prefix with `r`) to handle Windows file paths correctly.

## Usage

1. **Start the Application**
   - Run `python main.py`
   - A window opens with an empty label

2. **Click "Start Slideshow"**
   - Images begin cycling automatically
   - Each image displays for 3 seconds
   - Images loop infinitely

3. **View Images**
   - Images are resized to 1080×1080 pixels
   - Displayed in the center of the window
   - Click the window close button to exit

## Supported Image Formats

- **JPG / JPEG** - `.jpg`, `.jpeg`
- **PNG** - `.png`
- **AVIF** - `.avif`
- **WebP** - `.webp`
- **GIF** - `.gif` (static images only)
- **BMP** - `.bmp`

## Configuration

### Change Image Size

Modify the `image_size` variable:

```python
# Default: 1080x1080
image_size = (1080, 1080)

# Examples:
image_size = (800, 800)      # Smaller images
image_size = (1280, 1024)    # Different aspect ratio
```

### Change Delay Between Images

Modify the `root.after()` value (in milliseconds):

```python
# Default: 3000 ms (3 seconds)
root.after(3000, update_image)

# Examples:
root.after(2000, update_image)   # 2 seconds
root.after(5000, update_image)   # 5 seconds
```

## Image Processing Flow

```
Load image paths → Open images → Resize to 1080×1080 → Convert to PhotoImage
                                                              ↓
                                                      Display in Label
                                                              ↓
                                                       Wait 3 seconds
                                                              ↓
                                                     Show next image
                                                              ↓
                                                    Loop infinitely
```

## How It Works

1. **Image Loading**: All images are loaded at startup using PIL
2. **Image Conversion**: Images are converted to PhotoImage format for Tkinter
3. **GUI Setup**: A label widget displays the images
4. **Auto-Cycling**: Uses `root.after()` for non-blocking image updates
5. **Infinite Loop**: Uses modulo arithmetic to cycle back to the first image

## Example Setup

```python
image_paths = [
    r"C:\Users\gaura\Downloads\images\image1.jpg",
    r"C:\Users\gaura\Downloads\images\image2.jpg",
    r"C:\Users\gaura\Pictures\vacation.jpeg",
    r"C:\Users\gaura\Pictures\family.png",
]

# Images will display as:
# image1.jpg (3 sec) → image2.jpg (3 sec) → vacation.jpeg (3 sec) → family.png (3 sec) → image1.jpg (loop)
```

## Tips & Tricks

- **Organize Images**: Put all slideshow images in one folder for easy management
- **Fast Slideshow**: Reduce delay to 1000 ms (1 second) for rapid cycling
- **Slow Slideshow**: Increase delay to 5000 ms (5 seconds) for longer viewing
- **Uniform Size**: Ensure images are roughly square for best results at 1080×1080
- **Memory**: For large image collections, consider adding image limit logic

## Troubleshooting

### Issue: "FileNotFoundError: [Errno 2] No such file or directory"
- **Solution**: Check that all image paths are correct and files exist
- **Solution**: Use raw strings with `r` prefix for Windows paths

### Issue: Window opens but no images display
- **Solution**: Verify PIL/pillow is installed: `pip install pillow`
- **Solution**: Ensure image_paths list is not empty

### Issue: Images appear stretched or distorted
- **Solution**: Images are being resized to 1080×1080. For better results, use square images
- **Solution**: Adjust `image_size` to match your image aspect ratios

### Issue: Application runs slowly
- **Solution**: Images are loaded on startup. Many large images may cause delay
- **Solution**: Optimize image file sizes before adding to slideshow

## Enhancement Ideas

- Add pause/resume functionality
- Add next/previous image buttons
- Display current image number
- Add image information (filename, size)
- Add transitions between images
- Save favorite images
- Shuffle mode
- Full-screen mode

## System Requirements

- **OS**: Windows, macOS, Linux
- **RAM**: 256 MB minimum
- **Disk Space**: Depends on image size
- **Screen Resolution**: 1080×1080 minimum recommended

## Version
1.0

## License
Free to use and modify
