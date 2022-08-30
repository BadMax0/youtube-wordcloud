import os
import sys
from PIL import Image
import numpy as np
from wordcloud import WordCloud


def get_name(background, colormap, prefix):
    return os.path.join('results', f'{prefix}_{background}_{colormap}.png')


def create_wordcloud(background, colormap, words, width, height, prefix, mask=None, font=None):
    file_name = get_name(background, colormap, prefix)
    try:
        wordcloud = WordCloud(width=width,
                              height=height,
                              max_words=50,
                              background_color=background,
                              repeat=True,
                              max_font_size=300,
                              colormap=colormap,
                              mask=mask,
                              font_path=font).generate(words)
        wordcloud.to_file(get_name(background, colormap, prefix))
        print(file_name, '->', 'Created')
    except Exception as e:
        print('Error to create', file_name, e)


def create_banner(background, colormap, words, font=None):
    mask = np.array(Image.open('template.png'))
    create_wordcloud(background, colormap, words, 2048, 1152, 'banner', mask=mask, font=font)


def create_logo(background, colormap, words, font=None):
    create_wordcloud(background, colormap, words, 150, 150, 'logo', font=font)


def create_wordcloud_colormap(background, colormap, words, font=None):
    create_banner(background, colormap, words, font)
    create_logo(background, colormap, words, font)


def create_wordcloud_background(background, words, font=None):
    with open('colormaps.txt') as colormaps:
        for colormap in colormaps:
            create_wordcloud_colormap(background, colormap.replace('\n', ''), words, font=font)


def main(font):
    with open('words.txt', 'r', encoding='utf-8') as words_file:
        words = words_file.read()
        with open('backgrounds.txt') as backgrounds:
            for background in backgrounds:
                create_wordcloud_background(background.replace('\n',''), words, font=font)


if __name__ == '__main__':
    try:
        font = sys.argv[1]
    except IndexError:
        font = None
    main(font=font)