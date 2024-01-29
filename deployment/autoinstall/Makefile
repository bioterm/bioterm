
CI_FLES = meta-data user-data

meta-data:
	# Meta-Data can be empty file but must be present
	touch meta-data

test-seed-cd.iso: $(CI_FLES)
	# Generating ISO Image
	genisoimage -output $@ -volid CIDATA -joliet -rock $?

test-seed-vfat.img: $(CI_FLES)
	# Creating empty image for vfat
	truncate --size 64M $@
	# Formatting image
	mkfs.vfat -n CIDATA $@
	# Using mcopy (from mtools package)
	mcopy -ovi $@ $? ::/

clean:
	rm -f test-seed-cd.iso test-seed-vfat.img

build: test-seed-cd.iso test-seed-vfat.img

all: clean build

.PHONY: clean build all


all-temp: all
	mkdir -p /tmp/testseed/
	cp -vf test-seed* /tmp/testseed/
	chmod -R a+rX /tmp/testseed/