import random


def main(group):
	emoji = [
		['😔', '😢', '😞', '😩', '😡'],
		['🙁', '😥', '😟', '😓', '😠'],
		['😕', '😣', '😰', '😒', '😤'],
		['😐', '😩', '😖', '😑', '😾'],
		['😶', '😯', '😬', '😮', '😣'],
		['🙂', '😊', '😄', '😁', '😅'],
		['😆', '😂', '🤣', '😃', '😋'],
		['😇', '🥳', '🤩', '😍', '🌟']
	]

	stickers = [
		[
			"CAACAgIAAxkBAAECfHllf8hnH4BKqSeE0P1GjQI1hoGXogAC6BkAAvHpIElMUTQG1lAkfDME",
			"CAACAgIAAxkBAAECxuZlnknfWHoOCCFLcOyMg5YRSJ1kUQACUyoAAqcLsUgBF-mgMF8kLzQE",
			"CAACAgIAAxkBAAECxv5lnkuAOXOK3L5e5drDynHZHDK43gACAhYAAu34iEmgbTx0pPTj0jQE",
			"CAACAgIAAxkBAAECxuplnkoiziFRbsETcq7lJCzReye4PQAChhsAAls3KUl5v0DmuTqNmTQE",
			"CAACAgQAAxkBAAECxuxlnkoxvsW8rQJvkQlrkRY571-2EQACpQ0AAit1GFBqq5X67BDYqTQE"
		],
		[
			"CAACAgIAAxkBAAECfHdlf8hCzIt9J4G8yV-6Z8yKMbMkqwACMhgAAubVMUrwHJqAPt6cVDME",
			"CAACAgQAAxkBAAECxu5lnkpvJvjZ5JBUZtUs0yBDAckkSgACpwwAAjU7EFBPxdBoqm6aizQE",
			"CAACAgQAAxkBAAECxvBlnkp6pu0XcA5vtxYjf5cBRluVPwAC6QcAAmac6VPGkxqTsvVfgDQE",
			"CAACAgIAAxkBAAECxvJlnkrrOlMSdfECN9zfe8Yj9gqBIwACKAEAAhgVeAMAAUPlbcIn7Os0BA",
			"CAACAgIAAxkBAAECxuhlnkn7_Qn5lBxvdGD9tnvCXZFd_wACLQEAAhgVeAO70N1nwRRmEjQE"
		],
		[
			"CAACAgIAAxkBAAECfGtlf8ZUEC2KZrXIwxRY7PXSjXhc8gAChxcAAgwIIUlw7wJkhh8RGzME",
			"CAACAgIAAxkBAAECxvplnktNIONM_vLJ1SpHbkyWj-MXZwACvQ8AAqxiYUs_OLJh6zugJzQE",
			"CAACAgIAAxkBAAECxwABZZ5LnxbKPCnuRlSkxsF2sKQlkqEAAoQbAAI0RXBKkA_UKcZ0F_U0BA",
			"CAACAgQAAxkBAAECxwhlnkvIs89vlRWApDuiWfj7yqZ3VQAC3QkAAjANOVOxYze4AAFC2rc0BA",
			"CAACAgIAAxkBAAECxxxlnkwdf5fxf3rHyd1LsvINAAFVl0IAAiEAA-a7bhlbqiWUKTqBQzQE"
		],
		[
			"CAACAgIAAxkBAAECfH1lf8j8T64VzfkumV-K1_JOX0DBAQACJSYAAitfqEirqLZjBytafTME",
			"CAACAgIAAxkBAAECxyBlnkw91Gn0CMHHpraYV9xjwcvdeAACiQAD5rtuGWST4dsLGS2ZNAQ",
			"CAACAgIAAxkBAAECxyJlnkxf7dwpGIiOY1zDtzP9TJ_74wAC0iUAAiuSGUj9Z-GZMoTQ7zQE",
			"CAACAgIAAxkBAAECxyRlnkxnxKvcw1T810mL1T5mzzEuoQACiR4AAitEIUg6mFP6_nFR5DQE",
			"CAACAgIAAxkBAAECxzNlnkzOUHT2ZyVOF_vNDaz5LRTRVwACugAD5rtuGeq_6BkaJkisNAQ"
		],
		[
			"CAACAgIAAxkBAAECfH9lf8kKKMHTAAEWMrQoTvdhchbIPiYAAiQbAAISByBJFS9eruUGkeYzBA",
			"CAACAgIAAxkBAAECxvRlnksqxBdLYsoSbfJ_xs7mclIolAACbQEAAj0N6AQD0FG5NFLEwzQE",
			"CAACAgIAAxkBAAECxwZlnku8hvf1ga9tpebQcWtbfdytzQAC-xUAAjDyIEmILO94haYfRDQE",
			"CAACAgIAAxkBAAECxy9lnky5lv8_tDNucCbp79IPlbeP5wACoAAD5rtuGRDztwjXGYqLNAQ",
			"CAACAgIAAxkBAAECxzFlnkzFNxQm0ZGZ_bXgVFIAAQPRifAAAqIAA-a7bhnIT9d56sZcajQE"
		],
		[
			"CAACAgQAAxkBAAECfINlf8kruHU2TpB-1-5PZkMU8jYKOQADCgACCDfQU62EjbJsCr1ZMwQ",
			"CAACAgQAAxkBAAECxw5lnkvhOUMvq9yxa3Oi1vlYG8lIlwACMQgAAmBF2FD-5dqs6ryXsDQE",
			"CAACAgIAAxkBAAECxxJlnkv07MRzWXx99Xzv27a-lFfBagACEwADdVCBEzyG-hGvmFG4NAQ",
			"CAACAgIAAxkBAAECxxRlnkv7J12qt8pBy2OzJTG4FBnQtgACFAADdVCBE3vwB3oO6SFENAQ",
			"CAACAgIAAxkBAAECxxhlnkwJcn6Xcl3fNVIckb07Oj9o4AACvAAD5rtuGV9fbAHyRZNDNAQ"
		],
		[
			"CAACAgQAAxkBAAECfIFlf8ki8Fp-CY7QPIDyDjsuwTHL8AACEAsAAuY3OFNOHV2yQSpyPzME",
			"CAACAgIAAxkBAAECxvZlnks6FDFvrf3ZWeRMpzU5nM82MAACZQEAAj0N6ASMSuHCVTv68zQE",
			"CAACAgIAAxkBAAECxvxlnkth9aW33qAxFXArTyKTmDVE6QAC2wEAAj0N6ATV0xdK_crtUDQE",
			"CAACAgQAAxkBAAECxwplnkvUxLC1QbHVhmlk_x8QFMgXawACEwkAAmm02FPQNTaiZEvOfzQE",
			"CAACAgIAAxkBAAECxytlnkyDKkaCX7cQ-j1RlYy9-dbqogACUxgAAn3xOElzDlAnYitoszQE"
		],
		[
			"CAACAgIAAxkBAAECfHtlf8iJD3OlSyepE2SbRRTWY2_YkgAC9kIAAv3TsEsdWgq-OhKkJzME",
			"CAACAgIAAxkBAAECxvhlnktEOXuSVvsMmpPuwMY7NsUI1QACZgEAAj0N6ATjIfs_IluHGTQE",
			"CAACAgIAAxkBAAECxwRlnkuuf7x_4n3O-33s7kPzVoZncAACdBUAAl9msEl5vX_OqlTFGTQE",
			"CAACAgIAAxkBAAECxyllnkx1SOTp_uFtGs8pkf3bxO0ergACBRwAAqenOUmK65Ft7drFnDQE",
			"CAACAgIAAxkBAAECxy1lnkyOSU3bA_9GQZmuwfm6CfuWggACFhkAAsfNOUlXcPzdVpJi4jQE"
		]
	]

	selected_emoji = random.choice(emoji[group])
	selected_sticker = random.choice(stickers[group])

	return selected_emoji, selected_sticker


if __name__ == '__main__':
	main()
