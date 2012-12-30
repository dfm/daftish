.PHONY: docs

docs:
	rm -rf docs/_themes/daftish
	git checkout master daftish
	git mv daftish docs/_themes/daftish
	(cd docs;make dirhtml)
	cp -r docs/_build/dirhtml/* .
	git add .
	git commit -am "Updating documentation."
	git push origin gh-pages
