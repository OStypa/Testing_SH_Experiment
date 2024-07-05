# coding=utf-8
from otree.api import (
    BaseConstants, )


class Constants(BaseConstants):

    # ============================================================================================================= #
    #                                                                                                               #
    #                                                 DESIGN SETUP                                                  #
    #                                                                                                               #
    # ============================================================================================================= #

    # NUMBER OF PLAYERS =========================================================================== #
    #   Please specify how many players per market will participate.                                #
    players_per_group = 4

    # VALUATION VECTORS =========================================================================== #
    #   Different player types can have different valuation vectors for resources. Set the          #
    #   valuation vectors for each type and resource (Please keep in mind that the number of value  #
    #   vectors has to be a number that is completely divisible by the variable                     #
    #   "players_per_group"). E.g., if the market has three types and six resources, set the first  #
    #   six values within the list for a type to a number. Please stick to the scheme below.        #
    #   This app supports up to 10 types and 10 resources. Types are generated by id_in_group.      #
    #   This means that if you have 4 players and 2 types, players 1 and 2 are Type1, and           #
    #   players 3 and 4 are Type2.                                                                  #
    val18_t1 = [13, 18, 3, 8]
    val18_t2 = [13, 18, 8, 3]
    val18_t3 = [3, 18, 8, 13]
    val18_t4 = [8, 18, 3, 13]
    #   Set vectors for multiple types in the following way:
    #       val18_t2 = [85, 2, 2, 80, 50, 80, 80, 30, 80, 80]
    #       val18_t3 = [85, 2, 2, 80, 50, 80, 80, 30, 80, 80]
    #       val18_t4 = [85, 2, 2, 80, 50, 80, 80, 30, 80, 80]
    #       ...

    # prio18 OF RESOURCES OVER PARTICIPANTS =================================================== #
    #   Since this app models only the proposing side as active players, the prio18 of the      #
    #   resources over the players have to be specified. Please assign a priority vector for every  #
    #   resource. The length of each vector has to be equal to the number of players specified      #
    #   above. The structure is [<Player with Priority 1>, <Player with Priority 2>, ...]           #
    prio18_r1 = [2, 4, 1, 3]
    prio18_r2 = [3, 4, 2, 1]
    prio18_r3 = [4, 2, 1, 3]
    prio18_r4 = [1, 4, 2, 3]

    #   Set vectors for multiple resources in the following way:
    #       prio18_r2 = [1, 2]
    #       prio18_r3 = [1, 2]
    #       ...

    # RESOURCE CAPACITIES ========================================================================= #
    #   Set the quota of players that each resource can carry. Fill in as many number as in the     #
    #   valuation vectors.                                                                          #
    capacities = [1, 1, 1, 1]

    # ============================================================================================================= #
    #                                                                                                               #
    #                                                 APPEARANCE SETTINGS                                           #
    #                                                                                                               #
    # ============================================================================================================= #

    # FRAMING ===================================================================================== #
    #   Here you can choose between a neutral framing (participants/resources) and a application    #
    #   framing (participants/schools).                                                             #
    application_framing = True

    # SHOW INSTRUCTIONS =========================================================================== #
    #   Should the instructions for the mechanism be included?                                      #
    instructions = False

    # SHOW EXAMPLE IN INSTRUCTIONS ================================================================ #
    #   If "instructions = True", should the instructions also include a minimal example of the     #
    #   mechanism in place?                                                                         #
    instructions_example = False

    # SHOW CONFIRM BUTTON ========================================================================= #
    #   If "confirm_button" is set to "True", players will have to confirm their inputs made on     #
    #   Decision.html to. This can be used to avoid accidental submission of the page.              #
    confirm_button = False

    # SHOW RESULTS ================================================================================ #
    #   Should a results screen be included? The results screen shows a summary of results of the   #
    #   market (i.e., preferences submitted, bids made, clearing bids, allotted resources), and the #
    #   final payoff for the player.                                                                #
    results = True

    # ============================================================================================================= #
    #                                                                                                               #
    #                                                 INFORMATION SETTINGS                                          #
    #                                                                                                               #
    # ============================================================================================================= #

    # SHOW CAPACITIES ============================================================================= #
    #   If set to "True", the quota specified in "capacities" above will be shown to players on the #
    #   decision screen and in the instructions.                                                    #
    show_capacities = False

    # SHOW TYPES ================================================================================== #
    #   If "show_types" is set to "True", players will have a hint on the decision page and in the  #
    #   instructions that there are different types of players in the market. Only works if         #
    #   multiple type vectors have been specified above.                                            #
    show_types = True

    # SHOW OTHERS' val18 ===================================================================== #
    #   Should players see the other players' valuation profiles and on the decision page? Only     #
    #   works if "show_types" has been set to "True" above.                                         #
    show_val18 = True

    # SHOW RESOURCES' prio18 ================================================================== #
    #   Should a player see the resources' prio18 for her in the instructions and on the        #
    #   decision page?                                                                              #
    show_prio18 = False

    ####################################################################################################################
    ####################################################################################################################
    # ------------------------------              DO NOT MODIFY BELOW HERE              ------------------------------ #
    ####################################################################################################################
    ####################################################################################################################

    capacities = [i for i in capacities if i is not None]
    nr_courses = len(capacities)

    val18_list = ["val18_t" + str(i) for i in range(1, 11)]
    val18_raw = []
    for i in val18_list:
        if i in locals():
            val18_raw.append(locals()[i])

    val18 = []
    for i in val18_raw:
        val18.append([j for j in i if j is not None])

    prio18_list = ["prio18_r" + str(i) for i in range(1, 11)]
    prio18_raw = []
    for i in prio18_list:
        if i in locals():
            prio18_raw.append(locals()[i])

    prio18 = []
    for i in prio18_raw:
        prio18.append([j for j in i if j is not None])

    nr_types = len(val18)

    name_in_url = "SHda18"
    num_rounds = 1