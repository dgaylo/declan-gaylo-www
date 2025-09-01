all: icons thumbnails $(OUTPUTDIR)/avatar.jpg $(OUTPUTDIR)/avatar.webp

# Icons
ICON_SVG = logo.svg

.PHONY: icons
icons: $(OUTPUTDIR)/logo.svg $(OUTPUTDIR)/icon-80.png $(OUTPUTDIR)/icon-120.png $(OUTPUTDIR)/icon-180.png

$(OUTPUTDIR)/logo.svg: $(ICON_SVG)
	cp $< $@

$(OUTPUTDIR)/icon-%.png: $(ICON_SVG)
	convert -density 2400 -resize $*x$* $< -strip $@

# Thumbnails
.PHONY: thumbnails
thumbnails: $(OUTPUTDIR)/hiking4Ks-thumbnail.jpg $(OUTPUTDIR)/undergradthesis-thumbnail.jpg

$(OUTPUTDIR)/%-thumbnail.jpg: %.jpg
	convert -quality 85 -resize x416 $< $@


# Miscellaneous
$(OUTPUTDIR)/avatar.% : avatar.jpg
	convert -resize x800 -quality 85 $< $@
