from parsing import menu_parsing, game_parsing


if __name__ == '__main__':
    # link = "https://store.steampowered.com/"
    # all_cat = []
    # all_cat = menu_parsing.category_extract(link)
    # print(all_cat)
    
    ###
    # link = "https://store.steampowered.com/category/strategy_grand_4x/"
    # all_game = []
    # all_game = game_parsing.outer_link_extraction(link)
    # print(all_game)
    
    ###
    link = "https://store.steampowered.com/app/1142710/Total_War_WARHAMMER_III/"
    all_game = game_parsing.inner_link_extraction(link)
    print(all_game)
    
    