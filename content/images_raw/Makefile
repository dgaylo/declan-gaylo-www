all: icons thumbnails \
	 $(OUTPUTDIR)/avatar.jpg $(OUTPUTDIR)/avatar.webp \
	 $(OUTPUTDIR)/banner.jpg $(OUTPUTDIR)/banner.webp \
	 $(OUTPUTDIR)/seal_mit.png $(OUTPUTDIR)/seal_webb.png

# Icons
ICON_SVG = logo.svg

.PHONY: icons
icons: $(OUTPUTDIR)/logo.svg $(OUTPUTDIR)/icon.svg $(OUTPUTDIR)/icon-80.png $(OUTPUTDIR)/icon-120.png $(OUTPUTDIR)/icon-180.png

$(OUTPUTDIR)/logo.svg: $(ICON_SVG)
	cp $< $@

$(OUTPUTDIR)/icon.svg: $(ICON_SVG)
	cp $< $@

$(OUTPUTDIR)/icon-%.png: $(ICON_SVG)
	convert -density 2400 -resize $*x$* $< -strip $@

# Thumbnails
.PHONY: thumbnails
thumbnails: $(OUTPUTDIR)/hiking4Ks-thumbnail.jpg $(OUTPUTDIR)/undergradthesis-thumbnail.jpg

$(OUTPUTDIR)/%-thumbnail.jpg: %.jpg
	convert -quality 85 -resize x300 $< $@

$(OUTPUTDIR)/%-thumbnail.jpg: %.png
	convert -quality 85 -resize x300 $< $@


# Miscellaneous
$(OUTPUTDIR)/avatar.% : avatar.jpg
	convert -resize x400 -quality 85 $< $@

$(OUTPUTDIR)/banner.% : banner.jpg
	convert -resize 2500x $< $@

$(OUTPUTDIR)/seal_mit.% : seal_mit.png # MIT requires at least 300px
	convert -resize 300x -strip $< $@

$(OUTPUTDIR)/seal_webb.% : seal_webb.png
	convert -resize 300x -strip $< $@