import os
from PIL import Image
import numpy as np
from wordcloud import WordCloud


def get_name(background, colormap, prefix):
    return os.path.join('results', f'{prefix}_{background}_{colormap}.png')


def create_wordcloud(background, colormap, words, width, height, prefix, mask=None):
    wordcloud = WordCloud(width=width, height=height, max_words=50, background_color=background,
                          repeat=True, max_font_size=300, colormap=colormap, mask=mask).generate(words)
    file_name = get_name(background, colormap, prefix)
    wordcloud.to_file(get_name(background, colormap, prefix))
    print(file_name, '->', 'Created')


def create_banner(background, colormap, words):
    mask = np.array(Image.open('template.png'))
    create_wordcloud(background, colormap, words, 2048, 1152, 'banner', mask=mask)


def create_logo(background, colormap, words):
    create_wordcloud(background, colormap, words, 150, 150, 'logo')


def create_wordcloud_colormap(background, colormap, words):
    create_banner(background, colormap, words)
    create_logo(background, colormap, words)


def create_wordcloud_background(background, words):
    with open('colormaps.txt') as colormaps:
        for colormap in colormaps:
            create_wordcloud_colormap(background, colormap.replace('\n', ''), words)


def main():
    with open('words.txt', 'r', encoding='utf-8') as words_file:
        words = words_file.read()
        with open('backgrounds.txt') as backgrounds:
            for background in backgrounds:
                create_wordcloud_background(background.replace('\n',''), words)


if __name__ == '__main__':
    main()