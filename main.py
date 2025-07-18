from parsing import menu_parsing, game_parsing, game_info


if __name__ == '__main__':
    # link = "https://store.steampowered.com/"
    # all_cat = []
    # all_cat = menu_parsing.category_extract(link)
    # print(all_cat) #63 cat
    
    ###
    # link = "https://store.steampowered.com/category/strategy_grand_4x/"
    # all_game_info = []
    # all_game_info = game_parsing.outer_link_extraction(link)
    # print(all_game_info[1])
    
    ###
    link = "https://store.steampowered.com/app/1158310/Crusader_Kings_III"
    game_details = game_info.game_info_extraction(link)
    print(game_details)
    
    