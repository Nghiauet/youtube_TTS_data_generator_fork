from youtube_tts_data_generator import YTSpeechDataGenerator

# First create a YTSpeechDataGenerator instance:

generator = YTSpeechDataGenerator(dataset_name='audio_1', lang = "vi")

# Now create a '.txt' file that contains a list of YouTube videos that contains speeches.
# NOTE - Make sure you choose videos with subtitles.

generator.prepare_dataset('links.txt')
# The above will take care about creating your dataset, creating a metadata file and trimming silence from the audios.