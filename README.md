# Persian Normalizer 

Just a simple normalizer for Persian _Natural Language Processing_ based on the [Virastar](https://github.com/aziz/virastar) ruby gem.

## Differences with Virastar 

Virastar is written in [Ruby](http://ruby-lang.org) and it's a great tool for Rubyists (as well as me). But this project is completely written in python and each stage of normalization has its own method. 

This actually makes the process of normalization more accurate. 

## Methods 

* `fix_prefix(input_text)` :
Fixes prefixes "می" or "نمی" or "بی" and puts a half-space or ZWNJ after them.
* `fix_badchars(input_text)` : Fixes Arabic Kaf(ك) and Arabic Ya (ي) and replaces them with the Persian ones. 
* `fix_numbers(input_text)` : Replaces all English numerals with Persian numerals. 
* `fix_en_numbers(input_text)` : Makes numbers in an English phrase English again.
* `fix_whole_numbers(input_text)` : Just runs `fix_numbers` and `fix_en_numbers` on the given text.
