from image_processor import *

mountain_img = PPMImage.read_ppm("sample_images/img1.ppm")
# mountain_img.show_ppm()
# threshold(mountain_img).show_ppm()
PPMImage.jpg_to_ppm('sample_images/apple.jpeg', 'sample_images/apple.ppm')
ball_img = PPMImage.read_ppm('sample_images/balls.ppm')
ball_img.show_ppm()
# apple_img = PPMImage.read_ppm('sample_images/apple.ppm')
# colour_extract_from_ppm(ball_img, (230, 90, 60), tolerance=75).show_ppm()
# colour_extract_from_ppm(ball_img, (66, 100, 222), tolerance=75).show_ppm()
# brightness_extract_from_ppm(apple_img, target_brightness_range=[45, 250]).show_ppm()
crop_ppm(ball_img, 200, crop_option="heart").show_ppm()
# image.show_ppm()

#
# PPMImage.generate_white_ppm(width=100, height=100).show_ppm()
# PPMImage.generate_black_ppm(width=50, height=50).show_ppm()
# PPMImage.generate_random_ppm(width=200, height=200).show_ppm()
# PPMImage.generate_random_ppm(width=50, height=50).draw_ppm()

# transformations
# rotated_image1 = rotate_ppm(image, 30, clockwise=False).show_ppm()
# resize_ppm(image, new_width=150, new_height=150).show_ppm()
# flip(image).show_ppm()
# stretch_ppm(image, 2, height_factor=1).show_ppm()


# filters
# grayscale_filter(image).show_ppm()
# invert_filter(image).show_ppm()
# adjust_brightness(image, factor=5).show_ppm()
#
# snp_img = snp_noise(image, intensity=0.1)
# snp_img.show_ppm()
# median_filter(snp_img).show_ppm()


# steganography
# encrypt_message('sample_images/img1.ppm', 'sample_images/encrypted.ppm',
#                 message=input("Enter message to encrypt: "))
# try:
#     encrypted = PPMImage.read_ppm('sample_images/encrypted.ppm')
#     # encrypted.show_ppm()
#     print(decrypt_message('sample_images/encrypted.ppm', message_length=int(input("Enter message length: "))))
# except FileNotFoundError:
#     pass

# pipeline(ball_img, grayscale_filter_ppm, snp_noise_ppm, rotate_ppm, flip).show_ppm()
