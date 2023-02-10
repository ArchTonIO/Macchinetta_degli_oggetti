# MACCHINETTA DEGLI OGGETTI #

## A collection of webscraping algorithm to scrape specific e-commerce websites, getting prices, location, and details about the items. ##

#### The initial goal is to collect the largest possible amount of data about e-commerce sites that operates in the local boundaries ####
#### the next step is to elaborate all this data and make a well oiled pipeline that spits out the specific information we need ####

### The project structure should be like this: ###
>     MACCHINETTA DEGLI OGGETTI
>                |
>                |-.vscode/
>                |- utils/
>                |- commons/
>                |-.gitignore
>                |- cerco_e_trovo_ws/
>                |- ebay_ws/
>                |- subito_ws/
>                |- facebook_marketplace_ws/
>                |- amazon_ws/
>                |- ... (all the possible websites to scrape)

### Dependendencies: ###

>    * webdriver-manager 3.8.5
>    * selenium 4.7.2
>    * pandas 1.5.3

>In this moment the project is tested on Linux (Arch Linux),
>but it should work on Windows and MacOs too.
>Conda is used to manage the virtual environment and all the dependencies
>are installed using conda with conda-forge channel.

### This project is entirely written in Python 3.11.0, in compliance with the PEP-8 standards ###