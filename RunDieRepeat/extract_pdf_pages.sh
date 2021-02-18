#!/usr/bin/bash
# Extract a range of pages from a PDF a create a new one with thoses
# USAGE: ./extract_pdf_pages.sh $in.pdf $first_page $last_page $out.pdf
gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dFirstPage="$2" -dLastPage="$3" -sOutputFile="$4" "$1"
