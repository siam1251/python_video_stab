from vidstab import VidStab
import matplotlib.pyplot as plt

input_vid = 'ostrich.mp4'

stabilizer = VidStab()
stabilizer.gen_transforms(input_path=input_vid)

stabilizer.plot_trajectory()
plt.savefig('trajectory_plot.png')

stabilizer.plot_transforms()
plt.savefig('transforms_plot.png')

stabilizer.stabilize(input_path=input_vid, output_path='stable_video.avi', border_type='black')
stabilizer.stabilize(input_path=input_vid, output_path='rep_stable_video.avi', border_type='replicate', border_size=100)
stabilizer.stabilize(input_path=input_vid, output_path='ref_stable_video.avi', border_type='reflect', border_size=100)
stabilizer.stabilize(input_path=input_vid, output_path='wide_stable_video.avi', border_type='black', border_size=100)