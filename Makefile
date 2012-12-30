.PHONY: docs

docs:
	rm -rf docs/_themes/daftish
	git checkout master daftish
	git mv daftish docs/_themes/daftish
	rm docs/index.rst
	git checkout master README.rst
	git mv README.rst docs/index.rst
	(cd docs;make dirhtml)
	cp -r docs/_build/dirhtml/* .
	git add .
	git commit -am "Updating documentation."
	git push origin gh-pages
