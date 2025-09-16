Explain what task you struggled with the most, and how you overcame it.

Getting Open3D to behave on macOS was the hardest part. I hit missing libs, a segfault in the legacy RGB-D path, and import errors because Open3D pulls in Dash/Plotly and ML deps. I fixed it by pinning/installing the missing packages, switching to the tensor API (then converting to legacy to save), and muting viewer stderr. I added tiny progress prints and a simple bash runner, then pushed over SSH to the required clone branch.

Research NeRF analysis methods and write an overview of how it works in no longer than 2 paragraphs. 

NeRF models a scene as a continuous function that maps a 3D point and view direction to color and density. A small MLP (fed with positional encodings) approximates this function. During training, each pixel’s camera ray is sampled at many depths; the network’s outputs are composited with the volume-rendering equation to synthesize the pixel, and the result is compared to the ground-truth image. Hierarchical sampling (coarse→fine) focuses samples where density is high, improving sharpness and efficiency.

Write an overview of an aspect you found most interesting in no longer than 1 paragraph.

I loved how a simple stereo formula—depth = (f * baseline) / disparity—turns two flat images into a fly-through 3D world. The little touches made it feel real: flipping into Open3D’s coordinates, opening the viewer already close and centered, and printing “Created disparity map…” and “Created point cloud…” so I knew each stage worked. It’s a nice reminder that small engineering details can turn a fragile demo into a dependable pipeline.
