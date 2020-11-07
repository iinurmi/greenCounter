import cv2
import time
import os

def video_to_frames(input_loc, output_loc):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
       input_loc: Input video file.
       output_loc: Output directory to save the frames.
    Returns:
        None
    """
    try:
      os.mkdir(output_loc)
    except OSError:
      pass
# Log the time
    time_start = time.time()
  # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
# Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    amount = 0
    print ("Converting video..\n")
    success, frame = cap.read()
    success = True
# Start converting the video
    while success:
  # Extract the frame
  # Write the results back to output location.
        cap.set(cv2.CAP_PROP_POS_MSEC,(count*500))
        success, frame = cap.read()
        print("Read a new frame", success)
        if not success:
          break
        cv2.imwrite(output_loc + "/%#05d.jpg" % count, frame)
        count = count + 1
        amount = amount + 1
  # Log the time again
    time_end = time.time()
  # Release the feed
    cap.release()
  # Print stats
    print ("Done extracting frames.\n%d frames extracted" % amount)
    print ("It took %d seconds to convert." % (time_end-time_start))
    
if __name__=="__main__":
  input_loc = 'testvideo.MOV'
  output_loc = 'frames'
  video_to_frames(input_loc, output_loc)

