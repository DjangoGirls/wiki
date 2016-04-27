# Update source text of tutorial on Crowdin

1. Have [crowdin tool installed](https://crowdin.com/page/cli-tool): `pip install crowdin-cli-py`
2. Clone the [tutorial repository](https://github.com/DjangoGirls/tutorial) or pull from master to get the newest version on your machine.
3. If you're doing that for the first time, get `crowdin.yaml` file in [Drive](https://drive.google.com/a/sitarska.com/file/d/0B_sMcBckSgWqNk9xSGc4WmFsMFE/view?usp=sharing) and change `base_path` to match path on your machine.
4. Run `crowdin-cli upload sources`
5. Go to Django Girls Project's settings on [Crowdin](https://crowdin.com/project/django-girls-tutorial/settings).
6. Click on `TM & MT`, `Pre-translate` and `Via TM`.
7. Select `all languages` and `all files` and click on `Pre-translate`. It may take a while!

That's it! :tada:
