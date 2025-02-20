#!/bin/bash

# Rerun quarto
sassc styles.scss styles.css 
quarto render --to html

