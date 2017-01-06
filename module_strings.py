# -*- coding: utf-8 -*-
# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M 
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from datetime import datetime

strings = [
  ("no_string", "NO STRING!"),
  ("empty_string", " "),
  ("yes", "Yes."),
  ("no", "No."),
# Strings before this point are hardwired.  
  ("blank_string", " "),
  ("error_string", "ERROR!!!ERROR!!!!ERROR!!!ERROR!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!!"),
##  ("none", "none"),
  ("noone", "no one"),
##  ("nothing", "nothing"),
  ("s0", "{s0}"),
  ("blank_s1", " {s1}"),
  ("reg1", "{reg1}"),
  ("s50_comma_s51", "{s50}, {s51}"),
  ("s50_and_s51", "{s50} and {s51}"),
  #SW - modified Party to Ship
  #("s5_s_party", "{s5}'s Party"),
  ("s5_s_party", "{s5}'s Ship"),

  ("given_by_s1_at_s2", "Given by {s1} at {s2}"),
  ("given_by_s1_in_wilderness", "Given by {s1} whilst in the field"),
  ("s7_raiders", "{s7} Raiders"),

  ("bandits_eliminated_by_another", "The troublesome bandits have been eliminated by another party."),
  #("msg_battle_won","Battle won! Press tab key to leave..."),
  ("msg_battle_won","Battle won! Press tab key to leave..."),
  ("tutorial_map1","You are now viewing the overland map. Left-click on the map to move your party to that location, enter the selected planet, or pursue the selected party. Time will pause on the overland map if your party is not moving, waiting or resting. To wait anywhere simply press and hold down the space bar."),

  ("change_color_1", "Change Color 1"),
  ("change_color_2", "Change Color 2"),
  ("change_background", "Change Background Pattern"),
  ("change_flag_type", "Change Flag Type"),
  ("change_map_flag_type", "Change Map Flag Type"),
  ("randomize", "Randomize"),
  ("sample_banner", "Sample banner:"),
  ("sample_map_banner", "Sample map banner:"),
  ("number_of_charges", "Number of charges:"),
  ("change_charge_1",       "Change Charge 1"),
  ("change_charge_1_color", "Change Charge 1 Color"),
  ("change_charge_2",       "Change Charge 2"),
  ("change_charge_2_color", "Change Charge 2 Color"),
  ("change_charge_3",       "Change Charge 3"),
  ("change_charge_3_color", "Change Charge 3 Color"),
  ("change_charge_4",       "Change Charge 4"),
  ("change_charge_4_color", "Change Charge 4 Color"),
  ("change_charge_position", "Change Charge Position"),
  ("choose_position", "Choose position:"),
  ("choose_charge", "Choose a charge:"),
  ("choose_background", "Choose background pattern:"),
  ("choose_flag_type", "Choose flag type:"),
  ("choose_map_flag_type", "Choose map flag type:"),
  ("choose_color", "Choose color:"),
  ("accept", "Accept"),
  ("charge_no_1", "Charge #1:"),
  ("charge_no_2", "Charge #2:"),
  ("charge_no_3", "Charge #3:"),
  ("charge_no_4", "Charge #4:"),
  ("change", "Change"),
  ("plus", "+"),
  ("minus", "-"),
  ("color_no_1", "Color #1:"),
  ("color_no_2", "Color #2:"),
  ("charge", "Charge"),
  ("color", "Color"),
  ("flip_horizontal", "Flip Horizontal"),
  ("flip_vertical", "Flip Vertical"),
  ("hold_fire", "Hold Fire"),
  ("blunt_hold_fire", "Blunt / Hold Fire"),  

##  ("tutorial_camp1","This is training ground where you can learn the basics of the game. Use A, S, D, W keys to move and the mouse to look around."),
##  ("tutorial_camp2","F is the action key. You can open doors, talk to people and pick up objects with F key. If you wish to leave a town or retreat from a battle, press the TAB key."),
##  ("tutorial_camp3","Training Ground Master wishes to speak with you about your training. Go near him, look at him and press F when you see the word 'Talk' under his name. "),
##  ("tutorial_camp4","To see the in-game menu, press the Escape key. If you select Options, and then Controls from the in-game menu, you can see a complete list of key bindings."),
##  ("tutorial_camp6","You've received your first quest! You can take a look at your current quests by pressing the Q key. Do it now and check the details of your quest."),
##  ("tutorial_camp7","You've completed your quest! Go near Training Ground Master and speak with him about your reward."),
##  ("tutorial_camp8","You've gained some experience and weapon points! Press C key to view your character and increase your weapon proficiencies."),
##  ("tutorial_camp9","Congratulations! You've finished the tutorial of Mount&Blade. Press TAB key to leave the training ground."),

##  ("tutorial_enter_melee", "You are entering the melee weapon training area. The chest nearby contains various weapons which you can experiment with. If you wish to quit this tutorial, press TAB key."),
##  ("tutorial_enter_ranged", "You are entering the ranged weapon training area.  The chest nearby contains various ranged weapons which you can experiment with. If you wish to quit this tutorial, press TAB key."),
##  ("tutorial_enter_mounted", "You are entering the mounted training area. Here, you can try different kinds of weapons while riding a horse. If you wish to quit this tutorial, press TAB key."),

#  ("tutorial_usage_sword", "Sword is a very versatile weapon which is very fast in both attack and defense. Usage of one handed swords are affected by your one handed weapon proficiency. Focus on the sword and press F key to pick it up."),
#  ("tutorial_usage_axe", "Axe is a heavy (and therefore slow) weapon which can deal high damage to the opponent. Usage of one handed axes are affected by your one handed weapon proficiency. Focus on the axe and press F key to pick it up."),
#  ("tutorial_usage_club", "Club is a blunt weapon which deals less damage to the opponent than any other one handed weapon, but it knocks you opponents unconscious so that you can take them as a prisoner. Usage of clubs are affected by your one handed weapon proficiency. Focus on the club and press F key to pick it up."),
#  ("tutorial_usage_battle_axe", "Battle axe is a long weapon and it can deal high damage to the opponent. Usage of battle axes are affected by your two handed weapon proficiency. Focus on the battle axe and press F key to pick it up."),
#  ("tutorial_usage_spear", "Spear is a very long weapon which lets the wielder to strike the opponent earlier. Usage of the spears are affected by your polearm proficiency. Focus on the spear and press F key to pick it up."),
#  ("tutorial_usage_short_bow", "Short bow is a common ranged weapon which is easy to reload but hard to master at. Usage of short bows are affected by your archery proficiency. Focus on the short bow and arrows and press F key to pick them up."),
#  ("tutorial_usage_crossbow", "Crossbow is a heavy ranged weapon which is easy to use and deals high amount of damage to the opponent. Usage of crossbows are affected by your crossbow proficiency. Focus on the crossbow and bolts and press F key to pick them up."),
#  ("tutorial_usage_throwing_daggers", "Throwing daggers are easy to use and throwing them takes a very short time. But they deal light damage to the opponent. Usage of throwing daggers are affected byyour throwing weapon proficiency. Focus on the throwing daggers and press F key to pick it up."),
#  ("tutorial_usage_mounted", "You can use your weapons while you're mounted. Polearms like the lance here can be used for couched damage against opponents. In order to do that, ride your horse at a good speed and aim at your enemy. But do not press the attack button."),

##  ("tutorial_melee_chest", "The chest near you contains some of the melee weapons that can be used throughout the game. Look at the chest now and press F key to view its contents. Click on the weapons and move them to your Arms slots to be able to use them."),
##  ("tutorial_ranged_chest", "The chest near you contains some of the ranged weapons that can be used throughout the game. Look at the chest now and press F key to view its contents. Click on the weapons and move them to your Arms slots to be able to use them."),
##
##  ("tutorial_item_equipped", "You have equipped a weapon. Move your mouse scroll wheel up to wield your weapon. You can also switch between your weapons using your mouse scroll wheel."),

  ("tutorial_ammo_refilled", "Ammo refilled."),
  ("tutorial_failed", "You have been beaten this time, but don't worry. Follow the instructions carefully and you'll do better next time.\
 Press the Tab key to return to to the menu where you can retry this tutorial."),

  ("tutorial_1_msg_1","In this tutorial you will learn the basics of movement and combat.\
 In Mount&Blade you use the mouse to control where you are looking, and the WASD keys of your keyboard to move.\
 Your first task in the training is to locate the yellow flag in the room and move over it.\
 You can press the Tab key at any time to quit this tutorial or to exit any other area in the game.\
 Go to the yellow flag now."),
  ("tutorial_1_msg_2","Well done. Next we will cover attacking with weapons.\
 For the purposes of this tutorial you have been equipped with a blaster, lightsaber, and energy shield..\
 You can draw different weapons from your weapon slots by using the scroll wheel of your mouse.\
 In the default configuration, scrolling up pulls out your next weapon, and scrolling down pulls out your shield.\
 If you are already holding a shield, scrolling down will put your shield away instead.\
 Try changing your wielded equipment with the scroll wheel now. When you are ready,\
 go to the yellow flag to move on to your next task."),
  ("tutorial_1_msg_3","Excellent. The next part of this tutorial covers attacking with melee weapons.\
 You attack with your currently wielded weapon by using your left mouse button.\
 Press and hold the button to ready an attack, then release the button to strike.\
 If you hold down the left mouse button for a while before releasing, your attack will be more powerful.\
 Now draw your sword and destroy the four dummies in the room."),
  ("tutorial_1_msg_4","Nice work! You've destroyed all four dummies. You can now move on to the next room."),
  ("tutorial_1_msg_5","As you see, there is an archery target on the far side of the room.\
 Your next task is to use your blaster and shoot the target three times. Press and hold down the left mouse button to aim.\
 You can then fire by releasing the left mouse button. Note the targeting reticule in the centre of your screen,\
 which shows you the accuracy of your shot.\
 In order to achieve optimal accuracy, let fly your arrow when the reticule is at its smallest.\
 Try to shoot the target now."),
  ("tutorial_1_msg_6","Well done! You've learned the basics of moving and attacking.\
 With a little bit of practice you will soon master them.\
 In the second tutorial you can learn more advanced combat skills and face armed opponents.\
 You can press the Tab key at any time to return to the tutorial menu."),

  ("tutorial_2_msg_1","This tutorial will teach you how to defend yourself with a shield and how to battle armed opponents.\
 For the moment you are armed with nothing but a shield.\
 Your task is not to attack, but to successfully protect yourself from harm with your shield.\
 There is an armed opponent waiting for you in the next room.\
 He will try his best to knock you unconscious, while you must protect yourself with your shield\
 by pressing and holding the right mouse button.\
 Go into the next room now to face your opponent.\
 Remember that you can press the Tab key at any time to quit this tutorial or to exit any other area in the game."),
  ("tutorial_2_msg_2","Press and hold down the right mouse button to raise your shield. Try to remain standing for thirty seconds. You have {reg3} seconds to go."),
  ("tutorial_2_msg_3","Well done, you've succeeded in defending against an armed opponent.\
 The next phase of this tutorial will pit you and your shield against a force of enemy soldiers.\
 Move on to the next room when you're ready to face the soldiers."),
  ("tutorial_2_msg_4","Defend yourself from blaster bolts by raising your shield with the right mouse button. Try to remain standing for thirty seconds. You have {reg3} seconds to go."),
  ("tutorial_2_msg_5","Excellent, you've put up a succesful defence against soldiers.\
 There is a reward waiting for you in the next room."),
  ("tutorial_2_msg_6","In the default configuration,\
 the F key on your keyboard is used for non-violent interaction with objects and humans in the gameworld.\
 To pick up the sword on the altar, look at it and press F when you see the word 'Equip'."),
  ("tutorial_2_msg_7","A fine weapon! Now you can use it to deliver a bit of payback.\
 Go back through the door and dispose of the soldiers you faced earlier."),
  ("tutorial_2_msg_8","Very good. Your last task before finishing this tutorial is to face the infantry soldiers.\
 Go through the door now and show him your strength!"),
  ("tutorial_2_msg_9","Congratulations! You have now learned how to defend yourself with a shield and even had your first taste of combat with armed opponents.\
 Give it a bit more practice and you'll soon be a renowned warrior.\
 The next tutorial covers directional defence, which is one of the most important elements of Mount&Blade combat.\
 You can press the Tab key at any time to return to the tutorial menu."),

  ("tutorial_3_msg_1","This tutorial is intended to give you an overview of parrying and defence without a shield.\
 Parrying attacks with your weapon is a little bit more difficult than blocking them with a shield.\
 When you are defending with a weapon, you are only protected from one direction, the direction in which your weapon is set.\
 If you are blocking upwards, you will parry any overhead swings coming against you, but you will not stop thrusts or attacks to your sides.\
 Either of these attacks would still be able to hit you.\
 That's why, in order to survive without a shield, you must learn directional defence.\
 Go pick up up the quarterstaff now to begin practice."),
  ("tutorial_3_msg_2","By default, the direction in which you defend (by clicking and holding your right mouse button) is determined by the attack direction of your closest opponent.\
 For example, if your opponent is readying a thrust attack, pressing and holding the right mouse button will parry thrust attacks, but not side or overhead attacks.\
 You must watch your opponent carefully and only initiate your parry AFTER the enemy starts to attack.\
 If you start BEFORE he readies an attack, you may parry the wrong way altogether!\
 Now it's time for you to move on to the next room, where you'll have to defend yourself against an armed opponent.\
 Your task is to defend yourself successfully for thirty seconds with no equipment other than a simple staff.\
 Your staff's attacks are disabled for this tutorial, so don't worry about attacking and focus on your defence instead.\
 Move on to the next room when you are ready to initiate the fight."),
  ("tutorial_3_msg_3","Press and hold down the right mouse button to defend yourself with your staff after your opponent starts his attack.\
 Try to remain standing for thirty seconds. You have {reg3} seconds to go."),
  ("tutorial_3_msg_4","Well done, you've succeeded this trial!\
 Now you will be pitted against a more challenging opponent that will make things more difficult for you.\
 Move on to the next room when you're ready to face him."),
  ("tutorial_3_msg_5","Press and hold down the right mouse button to defend yourself with your staff after your opponent starts his attack.\
 Try to remain standing for thirty seconds. You have {reg3} seconds to go."),
  ("tutorial_3_msg_6","Congratulations, you still stand despite the enemy's best efforts.\
 The time has now come to attack as well as defend.\
 Approach the door and press the F key when you see the word 'Go'."),

  ("tutorial_3_2_msg_1","Your staff's attacks have been enabled again. Your first opponent is waiting in the next room.\
 Defeat him by a combination of attack and defence."),
  ("tutorial_3_2_msg_2","Defeat your opponent with your quarterstaff."),
  ("tutorial_3_2_msg_3","Excellent. Now the only thing standing in your way is one last opponent.\
 He is in the next room. Move in and knock him down."),
  ("tutorial_3_2_msg_4","Defeat your opponent with your staff."),
  ("tutorial_3_2_msg_5","Well done! In this tutorial you have learned how to fight ably without a shield.\
 Train hard and train well, and no one shall be able to lay a stroke on you.\
 In the next tutorial you may learn speeder bike riding and mounted combat.\
 You can press the Tab key at any time to return to the tutorial menu."),

  ("tutorial_4_msg_1","Welcome to the fourth tutorial.\
 In this sequence you'll learn about riding a speeder bike and how to perform various exercises while riding.\
 We'll start by getting you mounted up.\
 Approach the speeder bike, and press the 'F' key when you see the word 'Mount'."),
  ("tutorial_4_msg_2","While riding, the WASD keys control your speeder bike's movement, not your own.\
 Ride your speeder bike and try to follow the yellow flag around the course.\
 When you reach the flag, it will move to the next waypoint on the course until you reach the finish."),
  ("tutorial_4_msg_3","Very good. Next we'll cover attacking enemies while riding. Approach the yellow flag now."),
  ("tutorial_4_msg_4","Draw your weapon (using the mouse wheel) and destroy the four targets.\
 Try hitting the practice targets as you pass them at full speed -- this provides an extra challenge,\
 but the additional speed added to your blow will allow you to do more damage.\
 The easiest way of doing this is by pressing and holding the left mouse button until the right moment,\
 releasing it just before you pass the target."),
  ("tutorial_4_msg_5","Excellent work. Now let us try some target shooting while riding a speeder bike. Go near the yellow flag now."),
  ("tutorial_4_msg_6","Locate the shooting target beside the riding course and shoot it three times with your blaster.\
 Although you are not required to ride while shooting, it's recommended that you try to hit the target at various speeds and angles\
 to get a feel for how your speeder bike's speed and course affects your aim."),
  ("tutorial_4_msg_7","Congratulations, you have finished this tutorial.\
 You can press the Tab key at any time to return to the tutorial menu."),
# Ryan END

  ("tutorial_5_msg_1","TODO: Follow order to the flag"),
  ("tutorial_5_msg_2","TODO: Move to the flag, keep your units at this position"),
  ("tutorial_5_msg_3","TODO: Move to the flag to get the soldiers"),
  ("tutorial_5_msg_4","TODO: Move soldiers to flag1, infantry to flag2"),
  ("tutorial_5_msg_5","TODO: Enemy is charging. Fight!"),
  ("tutorial_5_msg_6","TODO: End of battle."),

  ("trainer_help_1", "This is a training ground where you can learn the basics of the game. Use A, S, D, W keys to move and the mouse to look around."),
  ("trainer_help_2", "To speak with the trainer, go near him, look at him and press the 'F' key when you see the word 'Talk' under his name.\
 When you wish to leave this or any other area or retreat from a battle, you can press the TAB key."),

#SW - modified custom battle descriptions 
  #("custom_battle_1", "Defend the village from an Imperial Attack!"),
  ("custom_battle_1", "Destroy the Endor Shield Generator!"),
  ("custom_battle_2", "Attack the Imperial Outpost!"),
  #("custom_battle_3", "Defend the Rebel Base from an Imperial Attack!"),
  ("custom_battle_3", "Survive an attack by Tusken Raiders!"),
  ("custom_battle_4", "Attack the Imperial Army!"),
  ("custom_battle_5", "Attack on the Yavin IV Shrine!"),
  ("custom_battle_8", "Assault the Imperial Spaceship!"),
  ("custom_battle_9", "Escape the Maze!"),

  ("finished", "(Finished)"),

  ("delivered_damage", "Delivered {reg60} damage."),
  ("archery_target_hit", "Distance: {reg61} yards. Score: {reg60}"),
  
  ("use_baggage_for_inventory","Use your baggage to access your inventory during battle (it's at your starting position)."),
##  ("cant_leave_now","Can't leave the area now."),
  ("cant_use_inventory_now","Can't access inventory now."),
  ("cant_use_inventory_arena","Can't access inventory in the arena."),
  ("cant_use_inventory_disguised","Can't access inventory while you're disguised."),
  ("cant_use_inventory_tutorial","Can't access inventory in the training camp."),
#SW - modified denar to credit
  ("1_denar", "1 credit"),
  ("reg1_denars", "{reg1} credits"),
#SW - modified months to be the star wars calendar 
  ("january_reg1_reg2", "Elona {reg1}, {reg2} ABY"),
  ("february_reg1_reg2", "Kelona {reg1}, {reg2} ABY"),
  ("march_reg1_reg2", "Selona {reg1}, {reg2} ABY"),
  ("april_reg1_reg2", "Telona {reg1}, {reg2} ABY"),
  ("may_reg1_reg2", "Nelona {reg1}, {reg2} ABY"),
  ("june_reg1_reg2", "Helona {reg1}, {reg2} ABY"),
  ("july_reg1_reg2", "Melona {reg1}, {reg2} ABY"),
  ("august_reg1_reg2", "Yelona {reg1}, {reg2} ABY"),
  ("september_reg1_reg2", "Relona {reg1}, {reg2} ABY"),
  ("october_reg1_reg2", "Welona {reg1}, {reg2} ABY"),
#last two months no longer used
#  ("november_reg1_reg2", "November {reg1}, {reg2}"),
#  ("december_reg1_reg2", "December {reg1}, {reg2}"),
  
##  ("you_approach_town","You approach the town of "),
##  ("you_are_in_town","You are in the town of "),
##  ("you_are_in_castle","You are at the castle of "),
##  ("you_sneaked_into_town","You have sneaked into the town of "),

  ("town_nighttime"," It is late at night and most citizens have abandoned the streets."),
  ("door_locked","The door is locked."),
  ("spacestation_is_abondened","The planet seems to be unoccupied."),
  ("town_is_abondened","The planet has no garrison defending it."),
  ("place_is_occupied_by_player","The place is held by your own troops."),
  ("place_is_occupied_by_enemy", "The place is held by hostile troops."),
  ("place_is_occupied_by_friendly", "The place is held by friendly troops."),

  ("do_you_want_to_retreat", "Are you sure you want to retreat?"),
  ("give_up_fight", "Give up the fight?"),
  #SW - new string for training
  ("give_up_training", "Do you wish to stop your training?"),
  ("do_you_wish_to_leave_tutorial", "Do you wish to leave the tutorial?"),
  ("do_you_wish_to_surrender", "Do you wish to surrender?"),
  ("can_not_retreat", "Can't retreat, there are enemies nearby!"),
##  ("can_not_leave", "Can't leave. There are enemies nearby!"),

  ("s1_joined_battle_enemy", "{s1} has joined the battle on the enemy side."),
  ("s1_joined_battle_friend", "{s1} has joined the battle on your side."),

#  ("entrance_to_town_forbidden","It seems that the town guards have been warned of your presence and you won't be able to enter the town unchallenged."),
  ("entrance_to_town_forbidden","The guards are on the lookout for intruders and it seems that you won't be able to pass through the shields unchallenged."),
  ("sneaking_to_town_impossible","The guards are alarmed. You wouldn't be able to sneak onto the planet no matter how well you disguised yourself."),

  ("battle_won", "You have won the battle!"),
  ("battle_lost", "You have lost the battle!"),

  #SW - modified
  # ("attack_walls_success", "After a bloody fight, your brave soldiers manage to claim the walls from the enemy."),
  # ("attack_walls_failure", "Your soldiers fall in waves as they charge the walls, and the few who remain alive soon rout and run away, never to be seen again."),
  # ("attack_walls_continue", "A bloody battle ensues and both sides fight with equal valour. Despite the efforts of your troops, the castle remains in enemy hands."),
  ("attack_walls_success", "After a bloody fight, your brave soldiers manage to take control of the planet from the enemy."),
  ("attack_walls_failure", "Your soldiers fall in waves as they charge the command center, and the few who remain alive soon rout and run away, never to be seen again."),
  ("attack_walls_continue", "A bloody battle ensues and both sides fight aggressively. Despite the efforts of your troops, the planet remains in enemy hands."),  

  ("order_attack_success", "Your men fight bravely and defeat the enemy."),
  ("order_attack_failure", "You watch the battle in despair as the enemy destroys your soldiers, then easily overwhelms the few remaining survivors."),
  ("order_attack_continue", "Despite an extended battle, your troops were unable to win a decisive victory."),

  ("join_order_attack_success", "Your men fight well alongside your allies, sharing in the glory as your enemies are beaten."),
  ("join_order_attack_failure", "You watch the battle in despair as the enemy destroys your soldiers, then easily overwhelms the few remaining survivors."),
  ("join_order_attack_continue", "Despite an extended battle, neither your troops nor your allies were able to win a decisive victory over the enemy."),

  ("siege_defender_order_attack_success", "The men of the garrison hold their walls with skill and courage, breaking the enemy assault and skillfully turning the defeat into a full-fledged rout."),
  ("siege_defender_order_attack_failure", "The assault quickly turns into a bloodbath. Valiant efforts are for naught; the overmatched garrison cannot hold the walls, and the enemy puts every last defender to the sword."),
  ("siege_defender_order_attack_continue", "Repeated, bloody attempts on the walls fail to gain any ground, but too many enemies remain for the defenders to claim a true victory. The siege continues."),


  ("hero_taken_prisoner", "{s1} of {s3} has been taken prisoner by {s2}."),
  ("hero_freed", "{s1} of {s3} has been freed from captivity by {s2}."),
  ("center_captured", "{s2} have taken {s1} from {s3}."),

  ("troop_relation_increased", "Your relation with {s1} has increased from {reg1} to {reg2}."),
  ("troop_relation_detoriated", "Your relation with {s1} has deteriorated from {reg1} to {reg2}."),
  ("faction_relation_increased", "Your relation with {s1} has increased from {reg1} to {reg2}."),
  ("faction_relation_detoriated", "Your relation with {s1} has deteriorated from {reg1} to {reg2}."),
  
  ("party_gained_morale", "Your party gains {reg1} morale."),
  ("party_lost_morale",   "Your party loses {reg1} morale."),

  ("qst_follow_spy_noticed_you", "The spy has spotted you! He's making a run for it!"),
  ("father", "father"),
  ("husband", "husband"),
  ("wife", "wife"),
  ("daughter", "daughter"),
  ("mother", "mother"),
  ("son", "son"),
  ("brother", "brother"),
  ("sister", "sister"),
  ("he", "He"),
  ("she", "She"),
  ("s3s_s2", "{s3}'s {s2}"),
  ("s5_is_s51", "{s5} is {s51}."),
  ("s5_is_the_ruler_of_s51", "{s5} is the ruler of {s51}. "),
  ("s5_is_a_nobleman_of_s6", "{s5} is a commander of {s6}. "),
##  ("your_debt_to_s1_is_changed_from_reg1_to_reg2", "Your debt to {s1} is changed from {reg1} to {reg2}."),

  ("relation_mnus_100", "Vengeful"), # -100..-94
  ("relation_mnus_90",  "Vengeful"),  # -95..-84
  ("relation_mnus_80",  "Vengeful"),
  ("relation_mnus_70",  "Hateful"),
  ("relation_mnus_60",  "Hateful"),
  ("relation_mnus_50",  " Hostile"),
  ("relation_mnus_40",  "  Angry"),
  ("relation_mnus_30",  "    Resentful"),
  ("relation_mnus_20",  "      Grumbling"),
  ("relation_mnus_10",  "        Suspicious"),
  ("relation_plus_0",   "         Indifferent"),# -5...4
  ("relation_plus_10",  "          Cooperative"), # 5..14
  ("relation_plus_20",  "           Welcoming"),
  ("relation_plus_30",  "            Favorable"),
  ("relation_plus_40",  "             Supportive"),
  ("relation_plus_50",  "              Friendly"),
  ("relation_plus_60",  "               Gracious"),
  ("relation_plus_70",  "                 Fond"),
  ("relation_plus_80",  "                  Loyal"),
  ("relation_plus_90",  "                   Devoted"),

  ("relation_mnus_100_ns", "{s60} is vengeful towards you."), # -100..-94
  ("relation_mnus_90_ns",  "{s60} is vengeful towards you."),  # -95..-84
  ("relation_mnus_80_ns",  "{s60} is vengeful towards you."),
  ("relation_mnus_70_ns",  "{s60} is hateful towards you."),
  ("relation_mnus_60_ns",  "{s60} is hateful towards you."),
  ("relation_mnus_50_ns",  "{s60} is hostile towards you."),
  ("relation_mnus_40_ns",  "{s60} is angry towards you."),
  ("relation_mnus_30_ns",  "{s60} is resentful against you."),
  ("relation_mnus_20_ns",  "{s60} is grumbling against you."),
  ("relation_mnus_10_ns",  "{s60} is suspicious towards you."),
  ("relation_plus_0_ns",   "{s60} is indifferent against you."),# -5...4
  ("relation_plus_10_ns",  "{s60} is cooperative towards you."), # 5..14
  ("relation_plus_20_ns",  "{s60} is welcoming towards you."),
  ("relation_plus_30_ns",  "{s60} is favorable to you."),
  ("relation_plus_40_ns",  "{s60} is supportive to you."),
  ("relation_plus_50_ns",  "{s60} is friendly to you."),
  ("relation_plus_60_ns",  "{s60} is gracious to you."),
  ("relation_plus_70_ns",  "{s60} is fond of you."),
  ("relation_plus_80_ns",  "{s60} is loyal to you."),
  ("relation_plus_90_ns",  "{s60} is devoted to you."),
  
  ("relation_reg1", " Relation: {reg1}"),

  ("center_relation_mnus_100", "The populace hates you with a passion"), # -100..-94
  ("center_relation_mnus_90",  "The populace hates you intensely"), # -95..-84
  ("center_relation_mnus_80",  "The populace hates you strongly"), 
  ("center_relation_mnus_70",  "The populace hates you"), 
  ("center_relation_mnus_60",  "The populace is hateful to you"), 
  ("center_relation_mnus_50",  "The populace is extremely hostile to you"), 
  ("center_relation_mnus_40",  "The populace is very hostile to you"), 
  ("center_relation_mnus_30",  "The populace is hostile to you"), 
  ("center_relation_mnus_20",  "The populace is against you"), 
  ("center_relation_mnus_10",  "The populace is opposed to you"), 
  ("center_relation_plus_0",   "The populace is indifferent to you"), 
  ("center_relation_plus_10",  "The populace is acceptive to you"), 
  ("center_relation_plus_20",  "The populace is cooperative to you"), 
  ("center_relation_plus_30",  "The populace is somewhat supportive to you"), 
  ("center_relation_plus_40",  "The populace is supportive to you"), 
  ("center_relation_plus_50",  "The populace is very supportive to you"), 
  ("center_relation_plus_60",  "The populace is loyal to you"), 
  ("center_relation_plus_70",  "The populace is highly loyal to you"), 
  ("center_relation_plus_80",  "The populace is devoted to you"), 
  ("center_relation_plus_90",  "The populace is fiercely devoted to you"),

  ("town_prosperity_0",   "The poverty of the planet of {s60} is unbearable"),
  ("town_prosperity_10",   "The squalorous planet of {s60} is all but deserted."),
  ("town_prosperity_20",   "The planet of {s60} looks a wretched, desolate place."),
  ("town_prosperity_30",   "The planet of {s60} looks poor and neglected."),
  ("town_prosperity_40",   "The planet of {s60} appears to be struggling."),
  ("town_prosperity_50",   "The planet of {s60} seems unremarkable."),
  ("town_prosperity_60",   "The planet of {s60} seems to be flourishing."),
  ("town_prosperity_70",   "The prosperous planet of {s60} is bustling with activity."),
  ("town_prosperity_80",   "The planet of {s60} looks rich and well-maintained."),
  ("town_prosperity_90",   "The planet of {s60} is opulent and crowded with well-to-do people."),
  ("town_prosperity_100",  "The glittering planet of {s60} openly flaunts its great wealth."),

  ("minorplanet_prosperity_0",   "The poverty of the planet of {s60} is unbearable."),
  ("minorplanet_prosperity_10",  "The planet of {s60} looks wretchedly poor and miserable."),
  ("minorplanet_prosperity_20",  "The planet of {s60} looks very poor and desolate."),
  ("minorplanet_prosperity_30",  "The planet of {s60} looks poor and neglected."),
  ("minorplanet_prosperity_40",  "The planet of {s60} appears to be somewhat poor and struggling."),
  ("minorplanet_prosperity_50",  "The planet of {s60} seems unremarkable."),
  ("minorplanet_prosperity_60",  "The planet of {s60} seems to be flourishing."),
  ("minorplanet_prosperity_70",  "The planet of {s60} appears to be thriving."),
  ("minorplanet_prosperity_80",  "The planet of {s60} looks rich and well-maintained."),
  ("minorplanet_prosperity_90",  "The planet of {s60} looks very rich and prosperous."),
  ("minorplanet_prosperity_100", "The planet of {s60}, looks immensely rich."),

  ("war_report_minus_4",   "we are about to lose the war"),
  ("war_report_minus_3",   "the situation looks bleak"),
  ("war_report_minus_2",   "things aren't going too well for us"),
  ("war_report_minus_1",   "we can still win the war if we rally"),
  ("war_report_0",   "we are evenly matched with the enemy"),
  ("war_report_plus_1",   "we have a fair chance of winning the war"),
  ("war_report_plus_2",   "things are going quite well"),
  ("war_report_plus_3",   "we should have no difficulty defeating them"),
  ("war_report_plus_4",   "we are about to win the war"),


  ("persuasion_summary_very_bad", "You try your best to persuade {s50},\
 but none of your arguments seem to come out right. Every time you start to make sense,\
 you seem to say something entirely wrong that puts you off track.\
 By the time you finish speaking you've failed to form a single coherent point in your own favour,\
 and you realise that all you've done was dig yourself deeper into a hole.\
 Unsurprisingly, {s50} does not look impressed."),
  ("persuasion_summary_bad",      "You try to persuade {s50}, but {reg51?she:he} outmanoeuvres you from the very start.\
 Even your best arguments sound hollow to your own ears. {s50}, likewise,\
 has not formed a very high opinion of what you had to say."),
  ("persuasion_summary_average",  "{s50} turns out to be a skilled speaker with a keen mind,\
 and you can't seem to bring forth anything concrete that {reg51?she:he} cannot counter with a rational point.\
 In the end, neither of you manage to gain any ground in this discussion."),
  ("persuasion_summary_good",     "Through quick thinking and smooth argumentation, you manage to state your case well,\
 forcing {s50} to concede on several points. However, {reg51?she:he} still expresses doubts about your request."),
  ("persuasion_summary_very_good","You deliver an impassioned speech that echoes through all listening ears like poetry.\
 The world itself seems to quiet down in order to hear you better .\
 The inspiring words have moved {s50} deeply, and {reg51?she:he} looks much more well-disposed towards helping you."),
  

# meet_spy_in_enemy_town quest secret sentences
  ("secret_sign_1",  "Do you want to go to Tosche Station to pick up some power converters?"),
  ("secret_sign_2",  "Can you speak Bocce?"),
  ("secret_sign_3",  "What is the possibility of successfully navigating an asteroid field?"),
  ("secret_sign_4",  "What do you know about Mos Eisley Cantina?"),
  
  ("countersign_1",  "No, I can't waste time with that until my chores are done"),
  ("countersign_2",  "Of course I can, sir. It’s like a second language to me."),
  ("countersign_3",  "Approximately three thousand seven hundred and twenty to one."),
  ("countersign_4",  "You will never find a more wretched hive of scum and villainy. You must be cautious."),

#SW - modified random names
# Names  
  ("name_1",  "Leyll"),
  ("name_2",  "Obran"),
  ("name_3",  "Kant"),
  ("name_4",  "Nimm"),
  ("name_5",  "Zan"),
  ("name_6",  "Ryssa"),
  ("name_7",  "Keylara"),
  ("name_8",  "Draze"),
  ("name_9",  "Kath"),
  ("name_10", "Myri"),
  ("name_11", "Harli"),
  ("name_12", "Niobe"),
  ("name_13", "Miwa"),
  ("name_14", "Xyras"),
  ("name_15", "Xyras"),
  ("name_16", "Moraine"),
  ("name_17", "Torent"),
  ("name_18", "Mara"),
  ("name_19", "Baz"),
  ("name_20", "Wyrren"),
  ("name_21", "Eskol"),
  ("name_22", "Ty"),
  ("name_23", "Rosh"),
  ("name_24", "Carth"),
  ("name_25", "Naz"),

# Surname
  ("surname_1",  "{s50} of Mandalore"),
  ("surname_2",  "{s50} of Christophsis"),
  ("surname_3",  "{s50} of Endor"),
  ("surname_4",  "{s50} of Carellia"),
  ("surname_5",  "{s50} of Naboo"),
  ("surname_6",  "{s50} of Kessel"),
  ("surname_7",  "{s50} of Dantooine"),
  ("surname_8",  "{s50} of Wayland"),
  ("surname_9",  "{s50} of Dac"),
  ("surname_10", "{s50} of Kashyyk"),
  ("surname_11", "{s50} of Hoth"),
  ("surname_12", "{s50} of Gamorr"),
  ("surname_13", "{s50} of Yavin IV"),
  ("surname_14", "{s50} of Tatooine"),
  ("surname_15", "{s50} of Manaan"),
  ("surname_16", "{s50} of Coruscant"),
  ("surname_17", "{s50} of Ryloth"),
  ("surname_18", "{s50} of Nal Hutta"),
  ("surname_19", "{s50} of Bespin"),
  ("surname_20", "{s50} of Dagobah"),
  ("surname_21", "{s50} the Nerf Herder"),
  ("surname_22", "{s50} the Sepper"),
  ("surname_23", "{s50} the Scruffy Looking"),
  ("surname_24", "{s50} the Bantha Fodder"),
  ("surname_25", "{s50} the Rocketjock"),
  ("surname_26", "{s50} the Tailhead"),
  ("surname_27", "{s50} the Bishwag"),
  ("surname_28", "{s50} the Madclaw"),
  ("surname_29", "{s50} the Blackboot"),
  ("surname_30", "{s50} the Junker"),
  ("surname_31", "{s50} the Spacer"),
  ("surname_32", "{s50} the Youngling"),
  ("surname_33", "{s50} the Bucket Head"),
  ("surname_34", "{s50} the Bughugger"),
  ("surname_35", "{s50} the Sodder"),
  ("surname_36", "{s50} the Codger"),
  ("surname_37", "{s50} the Smuggler"),
  ("surname_38", "{s50} the Rimmer"),
  ("surname_39", "{s50} the Fishhead"),
  ("surname_40", "{s50} the Flyboy"),
  ("surname_41", "{s50} the Mandie"),
  
  ("surnames_end", "surnames_end"),
  

  ("number_of_troops_killed_reg1", "Number of troops killed: {reg1}"),
  ("number_of_troops_wounded_reg1", "Number of troops wounded: {reg1}"),
  ("number_of_own_troops_killed_reg1", "Number of friendly troops killed: {reg1}"),
  ("number_of_own_troops_wounded_reg1", "Number of friendly troops wounded: {reg1}"),

  ("retreat", "Retreat!"),
  ("siege_continues", "Fighting Continues..."),
  ("casualty_display", "Your casualties: {s10}^Enemy casualties: {s11}{s12}"),
  ("casualty_display_hp", "^You were wounded for {reg1} hit points."),

# Quest log texts
  ("quest_log_updated", "Quest log has been updated..."),

  ("banner_selection_text", "You have been awarded the right to carry a banner.\
 Your banner will signify your status and bring you honor. Which banner do you want to choose?"),


# Retirement Texts: s7=village name; s8=castle name; s9=town name
  ("retirement_text_1", "Only too late do you realise that your money won't last.\
 It doesn't take you long to fritter away what little you bothered to save,\
 and you fare poorly in several desperate attempts to start adventuring again.\
 You end up a beggar in {s9}, living on a few credits and the charity of the church."),
  ("retirement_text_2", "Only too late do you realise that your money won't last.\
 It doesn't take you long to fritter away what little you bothered to save.\
 Once every credit has evaporated in your hands you are forced to start a life of crime in the backstreets of {s9},\
 using your skills to eke out a living robbing credits from women and poor citizens."),
  ("retirement_text_3", "Only too late do you realise that your money won't last.\
 It doesn't take you long to fritter away what little you bothered to save,\
 and you end up a poor drifter, going from cantina to cantina\
 blagging drinks from indulgent patrons by regaling them with war stories that no one ever believes."),
  ("retirement_text_4", "The credits you've saved doesn't last long,\
 but you manage to put together enough to buy some land near the planet of {s7}.\
 There you become a free farmer, and you soon begin to attract potential {wives/husbands}.\
 In time the villagers come to treat you as their local hero.\
 You always receive a place of honor at feasts, and your exploits are told and retold in the pubs and cantinas\
 so that the children may keep a memory of you for ever and ever."),
  ("retirement_text_5", "The credits you've saved doesn't last long,\
 but it's enough to buy a small cantina in {s9}. Although the locals are wary of you at first,\
 they soon accept you into their midst. In time your growing cantina becomes a popular feasthall and meeting place.\
 People come for miles to eat or stay there due to your sheer renown and the epic stories you tell of your adventuring days."),
  ("retirement_text_6", "You've saved wisely throughout your career,\
 and now your credits and your intelligence allow you to make some excellent investments to cement your future.\
 After buying several shops and warehouses in {s9}, your shrewdness turns you into one of the most prominent merchants on the planet,\
 and you soon become a wealthy {man/woman} known as much for your trading empire as your exploits in battle."),
  ("retirement_text_7", "As a landed noble, however minor, your future is all but assured.\
 You settle in your holdfast at {s7}, administrating the planet,\
 adjudicating the local courts and fulfilling your obligations to your leader.\
 Occasionally your leader calls you to assist and command allies in his campaigns, but these stints are brief,\
 and you never truly return to the adventuring of your younger days. You have already made your fortune.\
 With your own hall and holdings, you've few wants that your personal wealth and the income of your lands cannot afford you."),
  ("retirement_text_8", "There is no question that you've done very well for yourself.\
 Your extensive holdings and adventuring wealth are enough to guarantee you a rich and easy life for the rest of your days.\
 Retiring to your planet on {s8}, you exchange adventure for politics,\
 and you soon establish yourself as a considerable power in your leader's faction.\
 With intrigue to busy yourself with, your own lands to hunt, a hall to feast in and a hundred fine war stories to tell,\
 you have little trouble making the best of the years that follow."),
  ("retirement_text_9", "As a reward for your competent and loyal service,\
 your liege lord decrees that you be given a hereditary title, joining the major leaders of the realm.\
 Soon you complete your investitute as ruler of {s7}, and you become one of your leader's close advisors\
 and allies. Your renown garners you much subtle pull and influence as well as overt political power.\
 Now you spend your days playing the games of power, administering your great planets,\
 and recounting the old times of adventure and glory."),
  ("retirement_text_10", "Though you started from humble beginnings, your leader holds you in high esteem,\
 and a ripple of shock passes through the realm when he names you to the hereditary title of {ruler/ruler} of {s9}.\
 Vast planets and investments are now yours to rule. You quickly become your leader's most trusted advisor,\
 almost his equal and charged with much of the running of his realm,\
 and you sit upon a place of honor as one of the most powerful figures in the Galaxy."),


#NPC companion changes begin


# Objectionable actions

# humanitarian
  ("loot_village", "attack innocent villagers"),
  ("steal_from_villagers", "steal from poor villagers"),
  ("rob_caravan", "rob a merchant caravan"), # possibly remove
  ("sell_slavery", "sell people into slavery"),

# egalitarian
  ("men_hungry", "run out of food"), ##Done - simple triggers
  ("men_unpaid", "not be able to pay the men"),
#  ("party_crushed", "get ourselves slaughtered"), ##Done - game menus
  ("excessive_casualties", "turn every battle into a bloodbath for our side"),

# chivalric
  ("surrender", "surrender to the enemy"), ##Done - game menus
  ("flee_battle", "run from battle"), ##Done - game menus
  ("pay_bandits", "pay off bandits"),

# honest
  ("fail_quest", "fail a quest which we undertook on word of honor"),

# quest-related strings
  ("squander_money", "squander money given to us in trust"),
  ("murder_merchant", "involve ourselves in cold-blooded murder"),
  ("round_up_serfs", "round up servants on behalf of some commander"),


# Fates suffered by companions in battle
  ("battle_fate_1", "We were separated in the heat of battle"),
  ("battle_fate_2", "I was wounded and left for dead"),
  ("battle_fate_3", "I was knocked senseless by the enemy"),
  ("battle_fate_4", "I was taken and held for ransom"),
  ("battle_fate_5", "I got captured, but later managed to escape"),


# strings for opinion
  ("npc_morale_report", "I'm {s6} your choice of companions, {s7} your style of leadership, and {s8} the general state of affairs"), 
  ("happy", "happy about"),
  ("content", "content with"),
  ("concerned", "concerned about"),
  ("not_happy", "not at all happy about"),
  ("miserable", "downright appalled at"),  


  ("morale_reg1",    " Morale: {reg1}"),
  ("bar_enthusiastic", "                   Enthusiastic"),  
  ("bar_content",      "              Content"),
  ("bar_weary",        "          Weary"),
  ("bar_disgruntled",  "     Disgruntled"),
  ("bar_miserable",    "  Miserable"),  


#other strings
  ("here_plus_space", "here "),

#NPC strings
#npc1 = borcha
#npc2 = marnid
#npc3 = ymira  
#npc4 = rolf
#npc5 = baheshtur
#npc6 = firentis
#npc7 = deshavi
#npc8 = matheld
#npc9 = alayen
#npc10 = bunduk
#npc11 = katrin
#npc12 = jeremus
#npc13 = nizar
#npc14 = lazalit
#npc15 = artimenner
#npc16 = klethi

#SW - updated dialogs from patkelly
  ("npc1_intro", "Well, look what we have here.  Another mercenary, here in this great big galaxy, caught between the Empire and the Rebellion, just trying to make a buck and stay alive.  Look, I saw you sizing me up from the moment you walked in here, and I've got enough experience to know that means you're either about to fight me or hire me."),
  ("npc2_intro", "Yes?  How might this old man help you?"),
  ("npc3_intro", "Why, hello there!"),
  ("npc4_intro", "You're a captain right?  I saw your ship land.  She's a nice piece of work, cap'n, but that was one of the clumsiest landings I've ever seen.  I've got a proposition if you've got the time."),
  ("npc5_intro", "Greetings, spacefarer. Would you join me for a drink?"),
  ("npc6_intro", "Want a drink?  Of course you want a drink, you're in a cantina.  Here, friend, my treat. I just won a thousand credits playing pazaak against a particularly stupid Gamorrean.  Though here's a hint: when a piggy's dealing, say 'give me another card' instead of 'hit me.'"),
  ("npc7_intro", "Excuse me, are you a captain?  Could I have a moment with you?"),
  ("npc8_intro", "Drop your weapon.  You're under arrest."),
  ("npc9_intro", "No, you may not take a holovid of yourself with me.  Just be glad you saw the face of Arvis Xen with your own eyes, and leave me be."),
  ("npc10_intro", "A toast to war, to blood, to the thrill of unending combat!"),
  ("npc11_intro", "Please. You're an offworlder, I can tell from your voice. I haven't much time. The slavers are ruthless, and they stop at nothing to catch and punish escapees. One of us flayed and strung up keeps a hundred from escaping, they think."),
  ("npc12_intro", "So you're an actual captain of a real ship, huh?"),
  ("npc13_intro", "Greetings, friend! Can I interest you in a bona-fide, lab-tested, sure-fire Kashyyyk drop bear repellant?  Very dangerous, drop bears are.  Without repellant, you're just begging for a drop bear to come down on your head."),
  ("npc14_intro", "Yes? What is it you wish?"),
  ("npc15_intro", "Hello, there. Care to share a drink with me?"),
  ("npc16_intro", "Well, isn't this interesting?"),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_intro", ".........."),
  ("npc18_intro", ".........."),

  ("npc1_intro_response_1", "You're a sharp one."),
  ("npc2_intro_response_1", "You...the force is strong with you."),
  ("npc3_intro_response_1", "Er, hello.  You don't look the spacer type."),
  ("npc4_intro_response_1", "Perhaps. What manner of proposition?"),
  ("npc5_intro_response_1", "Certainly."),
  ("npc6_intro_response_1", "Thanks.  What's your story?"),
  ("npc7_intro_response_1", "Yes, what is it?"),
  ("npc8_intro_response_1", "You don't even have a blaster.  Why should I?"),
  ("npc9_intro_response_1", "I'm sorry, who did you say you were?"),
  ("npc10_intro_response_1", "To war!"),
  ("npc11_intro_response_1", "Nonsense, human slavery has been illegal for centuries."),
  ("npc12_intro_response_1", "Yes, I am?"),
  ("npc13_intro_response_1", "Please. Does anyone fall for that?"),
  ("npc14_intro_response_1", "To pass the time of day with a fellow traveller, if you permit."),
  ("npc15_intro_response_1", "Certainly, sir. With whom do I have the pleasure?"),
  ("npc16_intro_response_1", "Er, what's interesting?"),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_intro_response_1", "Power on the droid."),
  ("npc18_intro_response_1", "Power on the droid."),

  ("npc1_intro_response_2", "You forgot a third option: ignore you."),
  ("npc2_intro_response_2", "Nothing, never mind."),
  ("npc3_intro_response_2", "Run along now, girl. I have work to do."),
  ("npc4_intro_response_2", "Get out of here, sleemo."),
  ("npc5_intro_response_2", "I have no time for that."),
  ("npc6_intro_response_2", "I don't take drinks from people I don't know."),
  ("npc7_intro_response_2", "I'm sorry, I'm busy."),
  ("npc8_intro_response_2", "You've got to be kidding me.  Space off."),
  ("npc9_intro_response_2", "How pompous.  Get away from me."),
  ("npc10_intro_response_2", "I will do no such thing."),
  ("npc11_intro_response_2", "I haven't much time either. Get out of my sight."),
  ("npc12_intro_response_2", "That is none of your business."),
  ("npc13_intro_response_2", "Get out of here before I call the port authorities on you."),
  ("npc14_intro_response_2", "Nothing at all. My apologies."),
  ("npc15_intro_response_2", "No, thank you."),
  ("npc16_intro_response_2", "Not interesting enough."),
  #SW - new droid NPC's (copied personlity from npc6) 
  ("npc17_intro_response_2", "Leave the droid alone."),
  ("npc17_intro_response_2", "Leave the droid alone."),  

#backstory intro
  ("npc1_backstory_a", "Sharper than you know.  I've got some abilities few people have.  Abilities that cost more than your average merc's skill set.  Judging from the way you carry yourself, I think you know what I mean by that."),
  ("npc2_backstory_a", "Oh, is it now?  I must be getting sloppy in my old age. I thought I could hide my identity.  But if a whelp like you can sense me, that means the Emperor's Jedi hunters can sense me from a parsec away right now."),
  ("npc3_backstory_a", "Well, not yet I'm not!"),
  ("npc4_backstory_a", "I'm a pilot-navigator, and one of the best you'll see.  I can lay down hyperspace routes that hug gravity wells like a tight dress on a Twi'lek dancer.  I can make a bulk freighter maneuver like a TIE fighter."),
  ("npc5_backstory_a", "I am a gladiator, recently retired, having amassed a respectable 324-62 record in the pits of Gamorr.  Now I am seeing the galaxy I entertained for so long.  I travel from star system to star system, telling of my exploits and watching fights without the pressure of knowing that I will have to go against the winner.  It really is quite relaxing."),
  ("npc6_backstory_a", "My story? I'm a Corellian through and through.  I joined up with CorSec like my daddy before me.  My first raid, on a spice smuggling ring, went bad fast.  I took a stunner to the chest, and when I came to I was stashed with a bunch of my dead mates in a holding room."),
  ("npc7_backstory_a", "Ah. Yes.  Thank you."),
  ("npc8_backstory_a", "I am a bounty hunter, and you are my bounty!  ...wait, I don't have my blaster?  Oh, this will never do, it will never do.  How frustrating!"),
  ("npc9_backstory_a", "Surely you have heard of the wronged heir to the great Xen fortune!  Or if not, then you have heard my many swoop-racing triumphs, and have seen all competitors humiliated by my speed and my reflexes!  Or perhaps you are one of the millions to have lost your love's true affections once she gazed upon an image of my perfect face."),
  ("npc10_backstory_a", "Ahaha. Not often you'll see a captain who sees this galaxy the right way. So many just say, 'oh, I hope for peace.' Peace isn't the reason for this universe, any more than repairs are the reason we have ships. We exist to fight, and peace is only good for preparing ourselves for the next day's struggle!"),
  ("npc11_backstory_a", "I'm proof you're wrong. Sure, the Republic banned it, and the Empire doesn't allow it either. But the Empire doesn't hold the whole galaxy, and the sad little secret is that in a great number of its planets, the Galactic Empire stops where the spaceport ends. This galaxy is run by crime lords, with a thin coat of Imperial grey to pretty it up for the rich."),
  ("npc12_backstory_a", "Imagine my luck! I've only been in the spaceport a day and already I've met a real captain in flesh and blood!"),
  ("npc13_backstory_a", "Hey, you'd be surprised. With all the crazy stuff in this galaxy, half the people you meet will believe anything you tell 'em. After all, who's got time to visit every single planet to prove you wrong?  Heck, for all I know drop bears really do exist somewhere, and this spray can of water really does repel 'em.  It's not a lie if it might be true, eh?"),
  ("npc14_backstory_a", "Very well. I do not mind."),
  ("npc15_backstory_a", "I'm a librarian, plain and simple. Such is my trade, though I regret I have not had a chance to practice my trade in decades."),
  ("npc16_backstory_a", "Usually when a person talks to me, it's either because he is going to pay me to kill someone, because someone else has already paid me to kill him and he is begging me not to, or because he is very stupid and does not know exactly how dangerous it is to waste my time."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_backstory_a", "Hello, Master."),
  ("npc18_backstory_a", "Hello, Master."),  
  
#backstory main body
  ("npc1_backstory_b", "Maybe a hundred years ago, we'd have been classmates on Coruscant.  But the galaxy's a different place now, and there are different rules.  There's no good guys; there's just guys who'll shoot you and guys who'll pay you to shoot other guys.  I came to realize that's the galaxy I live in."),
  ("npc2_backstory_b", "I was a Jedi and a general of the Republic during the Clone Wars.  I fought the Empire tooth and nail, but soon I realized I was in too deep.  I went into hiding, and I've done a good job of it for a long time.  But you made me realize I can't hide much longer."),
  ("npc3_backstory_b", "I am a Jedi!  Well, I'm not really a Jedi.  In fact, I'm not entirely sure if I am anything of the sort at all.  But I do know that if I concentrate very hard on something, I think I can make it move.  I've spent a whole year practicing very hard."),
  ("npc4_backstory_b", "I joined the Empire like any good pilot.  234th TIE wing, designation DN-32-J.  Turns out, though, they just wanted to stick me in a backwater somewhere and make me fly boring non-stop patrols, scanning space dust hour and hour.  So I skipped out on my first R&R furlough, and went looking for a ticket back to the real action."),
  ("npc5_backstory_b", "Yes, I had been a gladiator until recently.  But recently, a man entered a cantina on the other side of the spaceport, and claimed he could fight and beat anyone.  I informed him, politely but firmly, that he was mistaken.  He swung his fist at me.  I punched him sharply in the chest, and he fell dead, his heart stopped cold. I am sure it was no murder, for I acted in self-defense.  However, the man was the son of the local security chief."),
  ("npc6_backstory_b", "After my capture, I saw opportunity.  I dumped my uniform, swapped clothes and ID with a dead smuggler, filled my pack with glitterstim, and set off.  That spice bought a pretty penny, and I've been drinking, gambling, and brawling across the galaxy ever since."),
  ("npc7_backstory_b", "I am Jade Codi, wife of Sothan Codi, Senator from Fondor.  Well, he was the Senator from Fondor, way back when.  I thought political life and old rivalries were behind us, but apparently an old unsettled score with a local crime lord finally caught up with us.  Sothan's dead now, and so I went into hiding."),
  ("npc8_backstory_b", "I spent two entire years trying to be a bounty hunter.  But yet I have not caught a single bounty.  Oh, it's not a matter of shooting, and it's not a matter of chasing.  I'm good at both.  I simply can't remember a face, captain.  Or much anything else, to be frank.  I can't tell a Sullustan from a Toydarian.  I once accidentally tried to turn my own aunt in for a bounty on Princess Leia of Alderaan.  But forgetting to bring my blaster to my attempt to capture you?  That's the last straw."),
  ("npc9_backstory_b", "I am the son of Vanam Xen, of the Xen Power-Core empire.  I didn't care much for the corporate life, so I spent my days as a swoop-racer, chasing fast fortunes and faster women. The swoopers called me a phony, sure, but they sure couldn't argue with my heat times. But then one day my parents disowned me, just because I slept with the wife of a business client. A couple bad bets and bad breaks on the track, and I ended up in the cantinas, with hardly a credit to my name."),
  ("npc10_backstory_b", "I'm a Mandalorian of the old line. I've fought in a hundred battles for a dozen sides. I've seen enough combat to know that's what we're here for. Politics, empires, rebellions, republics, planets, what have you. It's all the big dejarik board. The whole board is only there for that glorious moment when one piece strikes another. I've been around and everyone's told me they're fighting for peace. Well, I decided I won't fight for anyone who fights for peace."),
  ("npc11_backstory_b", "I was born a slave, daughter of a slave. When I was born, my duties were to be a playmate of my master's son.  When I was eight, my duties were to follow the boy, clean up for him, little things like that. When I became a young woman, well...I'm sure you understand. At twenty he sold me, and for the next twenty-five years I was a bound assistant to a sick, cruel man who called himself a doctor. But believe me, I am a slave no longer."),
  ("npc12_backstory_b", "I'm a nerf herder. Have been all my life.  Now I can already see the smile on your face, so drop it. If it weren't for us, your belly would be a lot leaner, and your crew a lot hungrier.  Anyways, I decided there was probably a galaxy beyond the fur and stink, so I sold my whole herd to buy transport offworld and to the nearest major spaceport."),
  ("npc13_backstory_b", "I'm a merchant by trade. I deal in the things that people only think they need. There are people out there who think they need to be prepared for every possible threat. So I make up a threat and then the cure. The way I look at it, a toy whistle I sell as a Drux Lizard call probably calls something somewhere, so it's not a complete lie. Unfortunately, I picked up a trail of angry customers who don't agree with me on that."),
  ("npc14_backstory_b", "I am a mercenary by trade, much as yourself, no doubt. And I have learned that the more you sweat your men, the more blood you'll save them and the more tears you'll save their wives. Unfortunately, the last captain I served as lieutenant to didn't see things quite the same way. I'm sure he regretted that when his men broke under pressure, tried to flee, and ended up taking Imperial blaster bolts to the back. Regret doesn't bring a man back, though, and I swore I'd never work for a soft captain again."),
  ("npc15_backstory_b", "I was a Jedi initiate once, back in the old days. I wasn't much for feeling the living Force, but I had a head for names, dates, and figures. A Jedi librarian, they made me, and I was a happy one. I focused my studies on architecture, a fascinating field, and became a good architect in my own right. After the Purge, I was able to leave the order and put my skills to use. Only now there's not much call for building; everyone just wants to tear things down. Well, I can do that too."),
  ("npc16_backstory_b", "I'm a hunter. A damn good hunter. Probably the best you'll see. I'm Echani, or at least half-Echani.  Can't speak for my father, I'm sure you know how it is.  But I can slip a vibroknife through whatever defenses you think you can offer. Darkness, seclusion, durasteel, blasters, lightsabers, whatever.  There's always a weak spot in their armor; there's always a sound in the shadows; there's always hole in their form."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_backstory_b", "I am a protocol droid trained in a variety of skills."),
  ("npc18_backstory_b", "I am a protocol droid trained in a variety of skills."),  
  
#backstory recruit pitch
  ("npc1_backstory_c", "It's a rough galaxy, with rough rules. So, are we going to be playing on the same team or not?"),
  ("npc2_backstory_c", "Well then, now that you know what I am, was there something you wished to ask me, or were you simply attempting to disturb an old Jedi trying to live his life in quiet peace?"),
  ("npc3_backstory_c", "See, look at your glass...Well, it didn't work that time, but I promise I've done it many times before!  I'm sure I just need to get off this world and get some experience, and I'll be a great Jedi yet!"),
  ("npc4_backstory_c", "So here's the deal.  Hire me and you've got yourself the best pilot in this sector, no strings attached."),
  ("npc5_backstory_c", "I am certain that he is as we speak plotting revenge.  I need a way off this planet."),
  ("npc6_backstory_c", "I mean, sure, it gets rough from time to time, but I can take on anyone in a fight.  Though that piggy's likely to bring back friends...hey, want an enforcer?  I'm probably going to need a ride off this rock soon anyway.  Might as well get paid for doing what I love, eh?"),
  ("npc7_backstory_c", "I need a ride off this planet and soon.  I've got a politician's tongue; I can get you the best deals for whatever your freighter is hauling.  I'll more than pay for my bunk."),
  ("npc8_backstory_c", "Look, I know I just tried to arrest you, but please, I'm not cut out for this work, captain.  And the Hutts have dropped thousands on my training and expenses, and I owe them a bounty or I'll owe them my head."),
  ("npc9_backstory_c", "Ring any bells?  Now unless you're here to buy holovid rights for a documentary on my engaging tragedy, or here to sponsor me for a race, leave me be."),
  ("npc10_backstory_c", "I'm not interested in the Imperials telling me they're fighting for order, or the Rebels saying they're fighting for liberty, or even the Hutts saying they're fighting for a buck. I'm interested in a captain who will fight the good fight for its own sake."),
  ("npc11_backstory_c", "He was a cruel man indeed; he treated those poor people who could afford no better, and...and he ordered me to mistreat patients so they would die and he could do...things...to them. I'll spare you the particulars, but my master is now deservedly dead and I am certain I will be hunted for it once they piece the bits of him back together."),
  ("npc12_backstory_c", "I'm looking to see the galaxy. I don't suppose you could give me a job on your crew?"),
  ("npc13_backstory_c", "Bring me aboard, friend, and I guarantee I'll repay you twenty times over. Sucker born every nanosecond in this galaxy, and if I could only get to other planets I'd get to sell to more of 'em."),
  ("npc14_backstory_c", "So, if you know of any captain who believes that the best way to protect his soldiers is to grind out the cowards and fools from their ranks, do let me know."),
  ("npc15_backstory_c", "I'm just looking for a steady income. If you need something built, I'll build it better and quicker than anyone else. If you need something brought down, well, that's not as rewarding, but I can do that too."),
  ("npc16_backstory_c", "But that's beside the point.  Client, prey, or fool: which are you?"),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_backstory_c", "What are your orders?"),
  ("npc18_backstory_c", "What are your orders?"),  

### use these if there is a short period of time between the last meeting
  ("npc1_backstory_later", "The same thing anyone does.  I'm getting by, and trying not to think of the consequences."),
  ("npc2_backstory_later", "I've been laying low as best I can, but I can't help but worry that I've lost my cover."),
  ("npc3_backstory_later", "Well, my self-training is coming along very well!  Just yesterday I was able to push a glass off the bar, and it fell and broke!  But I could not share my joy with anyone, for then I would have had to pay for the glass."),
  ("npc4_backstory_later", "I've been looking for a captain to get me off this rock, but no takers."),
  ("npc5_backstory_later", "I've been laying low, trying to avoid drawing attention to myself."),
  ("npc6_backstory_later", "Ha ha! I've been drinking, gambling, and fighting, and making enemies aplenty in the process.  Wouldn't mind a ticket to a new planet and a clean slate."),
  ("npc7_backstory_later", "I have been hiding, trying to avoid giving anyone any reason to suspect my identity.  I would happily join your freighter crew if you have an opening."),
  ("npc8_backstory_later", "I am trying desperately to come up with a bounty.  Time grows short, and the Hutts grow impatient."),
  ("npc9_backstory_later", "I've run a few street races, and I've won most of them.  But one loss is enough to cancel out ten wins. Fans like you don't understand that."),
  ("npc10_backstory_later", "I'm still looking for a captain who'll fight for all the right reasons."),
  ("npc11_backstory_later", "I've been hiding, of course. I hear rumors that they're after me, and I hear rumors that nobody even knows my master is dead yet. But when they find me, they will torture me, and they will kill me."),
  ("npc12_backstory_later", "I've been finding odd jobs, but I'm still looking for a career in the space lanes."),
  ("npc13_backstory_later", "I've come up with a great idea for a Alderaan Flu vaccine. All I need are some legit-looking needles and some clean water and I'm in business.  But you wouldn't be interested in helping me get offworld, would you?"),
  ("npc14_backstory_later", "I've gone from spaceport to spaceport, but still haven't found a captain who's willing to do what needs to be done to run a tight ship."),
  ("npc15_backstory_later", "I've been going from planet to planet, looking for takers for my services, but this isn't a galaxy where architecture is in high demand."),
  ("npc16_backstory_later", "Hunting.  Do you have a target for me?"),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_backstory_later", "Hello, Master. What are your orders?"),
  ("npc18_backstory_later", "Hello, Master. What are your orders?"),  

  ("npc1_backstory_response_1", "I like the way you think."),
  ("npc2_backstory_response_1", "Would you care to join my company of mercenaries?"),
  ("npc3_backstory_response_1", "A budding Force-sensitive is always welcome. We'll help you as best we can."),
  ("npc4_backstory_response_1", "I could use a good pilot."),
  ("npc5_backstory_response_1", "It sounds like you can fight.  I run a company of mercenaries."),
  ("npc6_backstory_response_1", "Sounds like you can bust heads. I could use an enforcer."),
  ("npc7_backstory_response_1", "Actually, I'm a merc.  Still interested?"),
  ("npc8_backstory_response_1", "Surely you aren't asking me to volunteer to be your bounty?"),
  ("npc9_backstory_response_1", "I don't know anything about swoops.  I'm a mercenary."),
  ("npc10_backstory_response_1", "You've got the right outlook. Fight with me, and we'll fight until the end."),
  ("npc11_backstory_response_1", "That's horrifying. I can get you off this planet."),
  ("npc12_backstory_response_1", "Well, you could travel with us, but you'd have to be able to fight."),
  ("npc13_backstory_response_1", "I might be able to use an extra hand, if you don't try to scam my crew."),
  ("npc14_backstory_response_1", "I might be able to use you in my crew."),
  ("npc15_backstory_response_1", "Well, we might have a use for you."),
  ("npc16_backstory_response_1", "I have a slightly different proposition, if you'll hear me out..."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_backstory_response_1", "Join my party."),
  ("npc18_backstory_response_1", "Join my party."),  
  
  ("npc1_backstory_response_2", "I'm sorry, but I don't think we'll be working together."),
  ("npc2_backstory_response_2", "I'm sorry to have bothered you."),
  ("npc3_backstory_response_2", "I'd rather not bring aboard a child with delusions of Force powers."),
  ("npc4_backstory_response_2", "I don't have a habit of hiring deserters."),
  ("npc5_backstory_response_2", "I have no interest in dealing with murderous muscleheads."),
  ("npc6_backstory_response_2", "Sorry, I'm not looking for a degenerate thug."),
  ("npc7_backstory_response_2", "I'm not interested in anyone with a bounty on their head."),
  ("npc8_backstory_response_2", "You are pathetic.  Get away from me."),
  ("npc9_backstory_response_2", "You're a self-absorbed washout. Bye."),
  ("npc10_backstory_response_2", "You're a bloodthirsty maniac.  I hope your death comes quickly."),
  ("npc11_backstory_response_2", "Your story is sad, but you are a murderer. Get away."),
  ("npc12_backstory_response_2", "Sorry. You're too scruffy-looking."),
  ("npc13_backstory_response_2", "No, sorry. I'd rather not pal around with a scammer."),
  ("npc14_backstory_response_2", "I'll let you know if I hear of anything. Goodbye."),
  ("npc15_backstory_response_2", "Sorry, we need soldiers, not scholars."),
  ("npc16_backstory_response_2", "I'm very sorry to waste your time."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_backstory_response_2", "I don't need your skills at this time."),
  ("npc18_backstory_response_2", "I don't need your skills at this time."),  
  
  ("npc1_signup", "All right then."),
  ("npc2_signup", "You're bold, asking that of a Jedi."),
  ("npc3_signup", "Really?  I will be able to travel and learn to harness my probably great powers?  Thank you!"),
  ("npc4_signup", "And you'll not find a better one elsewhere."),
  ("npc5_signup", "Why, that is a most generous offer."),
  ("npc6_signup", "Sounds good to me."),
  ("npc7_signup", "Oh, that's even better!"),
  ("npc8_signup", "No, no, no, of course not, of course not!  I'm not much of a bounty hunter, but I can shoot, and I can scrap in a close-up fight. Take me on to fight with you, and I'll put what credits I make towards repaying the Hutts."),
  ("npc9_signup", "Really?  That changes things.  That changes everything!"),
  ("npc10_signup", "Now that sounds like a place for me."),
  ("npc11_signup", "Will you? You're not going to turn me in for the bounty? Oh, thank you!"),
  ("npc12_signup", "Well, I don't know much about fighting in wars, but to be a good herder you have to be strong as a bull nerf and have the eye and the cunning of a manka cat. I reckon there's not much out there that's harder to fend off than a ravenous manka after your herd."),
  ("npc13_signup", "Sounds good, my friend, sounds good.  I'll even throw in an extra case of chrono-anomaly prevention wristbands if you upgrade me to first class!"),
  ("npc14_signup", "Well, I certainly wouldn't mind an opportunity to get back to the spacefaring life."),
  ("npc15_signup", "Well, I would certainly be happy to come along. If you plan on reducing an enemy stronghold, there's no sharper man for the job. If you need someone to build a school or a tower, so much the better."),
  ("npc16_signup", "...Oh, I see.  So you're a mercenary.  Well, now there's an interesting proposition indeed.  The petty crime lords and delinquent gamblers I usually hunt aren't a challenge at all.  They can't fight back.  Don't even know I'm coming.  I'm a hunter, and what I do here is scarcely hunting at all.  It's more murder, and murder isn't very interesting at all. "),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_signup", "Yes, Master."),
  ("npc18_signup", "Yes, Master."),  
  
  ("npc1_signup_2", "I don't need to sell you on my skills, I know a captain like you can tell more from looking than I could tell by talking.  Will we call it a partnership?"),
  ("npc2_signup_2", "But I know that unlike a clone or a droid, a mercenary can be trusted so long as he is paid.  His loyalty is to his wallet and not to the hidden schemes of some programmer.  And now that I know I can be sensed, I need loyal companions."),
  ("npc3_signup_2", "I think you would find I would be a most valuable addition to your ranks. I can sometimes levitate a cup for a little bit, I can occasionally push things around tables if I try very hard, and I know the names of many of the lightsaber fighting styles."),
  ("npc4_signup_2", "I'm the best pilot in this quadrant, bar none.  I can fly anything with engines.  I could make a pre-Imperial, rusted-through freight hauler outrun a Star Destroyer.  So what do you say?"),
  ("npc5_signup_2", "Though I have left the days of inflicting violence for credits behind, it seems now I must inflict violence to buy my own safety.  That is the way of this galaxy, it seems, and I appreciate your kind offer."),
  ("npc6_signup_2", "Though I should warn you, I'm not the type to just take it when people act out of line.  If someone steps on my toes, they get it in the face, right?  Tell your boys to keep off my back, and I'll watch yours."),
  ("npc7_signup_2", "The two-bit thugs after me wouldn't dare cross anyone capable of shooting back.  I'm not very familiar with a blaster, but I'm a quick study and I'll gladly learn anything you can teach me."),
  ("npc8_signup_2", "I understand if you don't trust me, but I swear to you now that I don't mean you harm.  Please.  I only look for a way to pay back the Hutts, and I can do that better as a mercenary under your wing than as a bounty hunter."),
  ("npc9_signup_2", "Look, I need my bank account back, and I don't care what I have to do to get it. I want what's mine, and when you're talking about fortunes the size of the one I'm talking about, tact goes out the window. I can ride, and I can shoot, but I need to learn how to command a crew and win a battle. I'll fight alongside you as long as you want. Then, I'll take what I've learned and take back my birthright."),
  ("npc10_signup_2", "You won't regret taking me on. I may not be as young as most soldiers, but I've got fifty years' worth of tactics in this head, and a warrior spirit that's sadly lacking in this galaxy."),
  ("npc11_signup_2", "I learned many things I'd like to forget over my life, but I've learned many things that will serve you well also. I can stabilize a critically wounded patient, I can administer field bacta treatments, and I can use a thin vibroblade to separate infected tissue. And to do other...similar things, as my master found out."),
  ("npc12_signup_2", "What I don't know, I can learn, and what I do know, nobody can teach. Give me an opportunity to show you what a nerf-herder can do out there, and you won't regret it."),
  ("npc13_signup_2", "And I can offer you a simple hardware upgrade that will triple your engine efficiency if you only..."),
  ("npc14_signup_2", "I'm a career soldier, born and bred for fighting. And I can take a rabble of soft misfits and turn them into soldiers nearly as good as I am, if you're willing to work the weakness out of them."),
  ("npc15_signup_2", "I can take care of myself with a blaster or a lightsaber, too.  I may be an architect by trade, but I've still got Jedi training when you get down to it."),
  ("npc16_signup_2", "Well, if the pay's good, and if you promise me the opportunity to use my skills on a regular basis,  I'm all yours, captain."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_signup_2", "Shall I meet you at the ship?"),
  ("npc18_signup_2", "Shall I meet you at the ship?"),  

  ("npc1_signup_response_1", "Then it's a partnership."),
  ("npc2_signup_response_1", "I would be happy to travel with you."),
  ("npc3_signup_response_1", "Well, that's a start.  I think we can help you with the rest."),
  ("npc4_signup_response_1", "Then I think we have a deal."),
  ("npc5_signup_response_1", "Certainly.  Let us be on our way."),
  ("npc6_signup_response_1", "There won't be any problems. Get your things in order."),
  ("npc7_signup_response_1", "Welcome aboard, then."),
  ("npc8_signup_response_1", "So long as I keep you pointed in the right direction, I think you'll work well."),
  ("npc9_signup_response_1", "Sure.  Meet me at my ship and we'll get started."),
  ("npc10_signup_response_1", "You'll find that spirit in my company. Welcome aboard."),
  ("npc11_signup_response_1", "You will be welcome on our ship."),
  ("npc12_signup_response_1", "Then welcome to our company, nerf-herder."),
  ("npc13_signup_response_1", "You do realize that we are mercenaries and not simple traders, right?"),
  ("npc14_signup_response_1", "Good. I'll be happy to hire someone like you."),
  ("npc15_signup_response_1", "That works for me. I will be happy to hire you."),
  ("npc16_signup_response_1", "It sounds like you can do the job. You're hired."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_signup_response_1", "Yes."),
  ("npc18_signup_response_1", "Yes."),  

#11
  ("npc1_signup_response_2", "I'm sorry, but I don't think I can use you."),
  ("npc2_signup_response_2", "I do not want to risk bringing aboard a Jedi who cannot disguise himself."),
  ("npc3_signup_response_2", "Actually, that doesn't sound particularly useful."),
  ("npc4_signup_response_2", "Actually, I do not want to take the risk of hiring a deserter."),
  ("npc5_signup_response_2", "On second thought, a hot-tempered gladiator does not sound like a safe companion."),
  ("npc6_signup_response_2", "Actually, a mercenary life is a hard one.  I don't think you have the discipline for it."),
  ("npc7_signup_response_2", "A price on your head is bad enough, but if you can't even fight you're no good to me."),
  ("npc8_signup_response_2", "I'm not going to hire anyone who tried to capture me for a bounty."),
  ("npc9_signup_response_2", "I don't need a self-important swoop jockey pretending to be a soldier."),
  ("npc10_signup_response_2", "On second thought, too much bloodthirstiness can be a bad thing."),
  ("npc11_signup_response_2", "Your story is tragic, but you need counseling, not combat."),
  ("npc12_signup_response_2", "Dodging a blaster bolt ain't like shooing pests, kid.  You're in over your head."),
  ("npc13_signup_response_2", "On second thought, I can't stand you.  Get out of here."),
  ("npc14_signup_response_2", "Actually, I have no wish to provoke a mutiny in my crew. Good day, sir."),
  ("npc15_signup_response_2", "Actually, I need a different kind of expertise. My apologies."),
  ("npc16_signup_response_2", "On second thought, you seem a bit too dangerous."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_signup_response_2", "Actually, I don't need your skills at this time."),
  ("npc18_signup_response_2", "Actually, I don't need your skills at this time."),  
  
  ("npc1_payment", "All right then. {reg3} credits, and we'll call it a deal.  Are we in, or are you going to walk out that door alone?"),
  ("npc2_payment", "."),
  ("npc3_payment", "."),
  ("npc4_payment", "Sounds good, sounds very good. Just one more thing before we leave.  The last captain I asked for a job decided to head off to see what kind of bounty an Imperial deserter would fetch.  I know a few people who can clear my record, but I'm going to need {reg3} credits to grease a few palms before I can show my face in public"),
  ("npc5_payment", "Thank you. Though I appreciate what you have offered to do for me, I'm going to have to ask for {reg3} credits before I can go with you.  I'm going to need to buy a false ID if I want to get off this planet without any undue entanglements."),
  ("npc6_payment", "."),
  ("npc7_payment", "All right then. I will come with you. But I would very much like a payment of {reg3} credits first.  I have recently pawned a family heirloom, and I could not leave this planet without it."),
  ("npc8_payment", "Great!  I promise I won't let you down! ...but, there is one problem. Before I can get off the system, I need {reg3} credits. As a down payment, see.  If the Hutts think I'm skipping out on them, I'll be a risk to you and your entire crew."),
  ("npc9_payment", "Good, good...but I confess I promised a particularly enthralling Twi'lek dancer I'd win a race for her tonight, and I'm short the {reg3} credit entry fee.  If you can cover me, it'd mean a lot to me."),
  ("npc10_payment", "That's good news. But I'll ask for one last thing, captain. I have a woman in the residential sector, and she says she has my child in her belly. I want to give her some money before I leave... for the child, you know. I don't want it growing up weak. Do you think you can spare {reg3} credits?"),
  ("npc11_payment", "Thank you so much. I know I've asked so much, but could I please ask for {reg3} credits more? I have only remained hidden over the last two weeks through the charity of the barkeep's family, and I should very much like to ensure they are repaid before I leave."),
  ("npc12_payment", "."),
  ("npc13_payment", "Ah, well, no, I was not.  In that case, I am still willing to come aboard, as I think my life will be equally in danger here once my customers grow a brain cell or two.  All I will ask is a mere {reg3} credits to cover a little insurance policy, and I will call you my captain."),
  ("npc14_payment", "Ah, one last thing. I would ask for an initial bounty of {reg3} credits before I join your command. It's my principle never to enter someone's service without receiving the payment I deserve."),
  ("npc15_payment", "Good. By the way, as a skilled architect I would expect a payment for my services. A signing bonus of {reg3} credits would be fair, I think."),
  ("npc16_payment", "Not that fast, I'm not.  I said 'if the pay's good', and in my line of work, we get paid up front.  If you want me to leave this cantina with you, it'll cost you {reg3} credits in addition to my weekly expenses. If you can pay it, we have a deal.  If you can't, then I think you should stop looking at merchandise you can't afford, captain."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_payment", "."),
  ("npc18_payment", "."),  
  
  ("npc1_payment_response", "Certainly. Here's your payment, partner."),
  ("npc2_payment_response", "."),
  ("npc3_payment_response", "."),
  ("npc4_payment_response", "Certainly. Here's {reg3} credits."),
  ("npc5_payment_response", "Well... here's {reg3} credits, then. Meet me on the ship."),
  ("npc6_payment_response", "."),
  ("npc7_payment_response", "I understand completely. Here's {reg3} credits."),
  ("npc8_payment_response", "I understand. Here are {reg3} credits. Go get your affairs in order."),
  ("npc9_payment_response", "Well, here's your credits, but the next races are on your own credstick."),
  ("npc10_payment_response", "Of course. Here, {reg3} credits."),
  ("npc11_payment_response", "Of course. Take these {reg3} credits, and get on the ship. We leave soon."),
  ("npc12_payment_response", "."),
  ("npc13_payment_response", "Of course, here's {reg3} credits. Make ready to leave soon."),
  ("npc14_payment_response", "All right, here's {reg3} credits. You are most welcome in our company."),
  ("npc15_payment_response", "All right, here's {reg3} credits. Glad to have you with us."),
  ("npc16_payment_response", "All right, here's {reg3} credits for you. Make yourself ready."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_payment_response", "."),
  ("npc18_payment_response", "."),  

  ("npc1_morality_speech", "Oy -- boss. Please don't take this the wrong way, but it's a hard life and it's a bit much that we {s21}. Take a little more care in the future, captain, if you don't mind my saying."),
  ("npc2_morality_speech", "I hope you don't mind my saying so, but it's a bit hard for me to see us {s21}. Maybe I ought to try to be more of a hardened soldier, but if we could try to exercise a little mercy from time to time, I'd sleep better."),
  ("npc3_morality_speech", "Perhaps it is not my place to say so, {sir/madame}, but I confess that I am somewhat shocked that we {s21}. Of course I realize that war is cruel, but there is no need to make it more cruel than necessary."),
  ("npc4_morality_speech", "Your pardon -- just so you know, the men of the House of Rolf do not care to {s21}. I will not be pleased if you continue to take this course."),
  ("npc5_morality_speech", "Pardon me, captain. It is not good to {s21}. Your first duty is to the men who have taken your salt. The least they can expect is food, pay, the opportunity to loot, and that you not waste their lives needlessly."),
  ("npc6_morality_speech", "Excuse me, {sir/madame}. As you know, I joined with you to right wrongs, protect the innocent, and make amends for my sin. I did not expect to {s21}."),
  ("npc7_morality_speech", "Captain -- I do not like to see us {s21}. Such are the actions of a common bandit chief, with no regard for his followers."),
  ("npc8_morality_speech", "I was not pleased that you decided to {s21}. To fall in battle is an honour, but to fight in a warband led by a coward is a disgrace."),
  ("npc9_morality_speech", "{Sir/Madame} -- it is not my way to {s21}. Men of my house will accept death but not dishonour. Please do not make me ashamed to serve under you."),
  ("npc10_morality_speech", "Begging your pardon, captain. I can't say that I'm happy to see us {s21}. Those are just simple people, trying to make a living. If we could try to go easy on the poor wretches, captain, I'd feel much better."),
  ("npc11_morality_speech", "Excuse me, captain. It's not good that we {s21}. I've followed armies and warbands for 30 years, and the least the soldiers expect of a leader is to feed them, pay them, and do {his/her} best to keep their sorry skins intact as best {he/she} can."),
  ("npc12_morality_speech", "Captain -- I do not like to see us {s21}. I am prepared to be a warrior, but not a brigand. Pray let us try to show a little more compassion."),
  ("npc13_morality_speech", "Captain, if we can avoid it, I'd prefer not to {s21}. In this Galaxy news travels fast, and one's reputation is precious. I would not care for one of my rivals to include this latest unfortunate incident in a satirical verse."),
  ("npc14_morality_speech", "I do not care to {s21}. No one with a reputation for cowardice will be properly feared by his men."),
  ("npc15_morality_speech", "{Sir/Madame} -- just so you know my opinion, any commander with sense will not let his company {s21}.I hope you don't mind me speaking so bluntly."),
  ("npc16_morality_speech", "Captain. I don't like to {s21}. So many throats left uncut, and so many purses left unexplored..."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_morality_speech", "Master, you should be aware that some of your behavior may violate Galactic Law."),
  ("npc18_morality_speech", "Master, you should be aware that some of your behavior may violate Galactic Law."),  

  ("npc1_2ary_morality_speech", "Boss -- just so you know, I've got no problem if we {s21}. Living to fight another day makes good sense to me."),
  ("npc2_2ary_morality_speech", "{Sir/Madame} -- I'm not altogether happy that we {s21}. I'm a merchant, and in our business one is bonded by one's word. I don't want a reputation for dishonesty -- that would spell my end as a trader, {sir/madame}."),
  ("npc3_2ary_morality_speech", "{Sir/Madame} -- I think it was a brave decision you took to {s21}. There is no shame in finding a way to avoid the spilling of blood."),
  ("npc4_2ary_morality_speech", "Your pardon -- whatever anyone else says, I think nothing of it that you {s21}. You should adopt whatever ruse you need to survive in these troubled times."),
  ("npc5_2ary_morality_speech", "[No secondary moral code]"),
  ("npc6_2ary_morality_speech", "{Sir/Madame} -- you may choose to {s21}, but would prefer to have no part in it. Such is not the path to my redemption."),
  ("npc7_2ary_morality_speech", "[No secondary moral code]"),
  ("npc8_2ary_morality_speech", "[No secondary moral code]"),
  ("npc9_2ary_morality_speech", "Captain, I am dismayed that you {s21}. A {gentleman/gentlewoman} such as yourself should exhibit the highest standards of honour at all times."),
  ("npc10_2ary_morality_speech", "{Brother/Sister} -- I can't say I like to see us {s21}. You should treat your men well, and they'll repay with interest."),
  ("npc11_2ary_morality_speech", "[No secondary moral code]"),
  ("npc12_2ary_morality_speech", "[No secondary moral code]"),
  ("npc13_2ary_morality_speech", "[No secondary moral code]"),
  ("npc14_2ary_morality_speech", "Captain -- you should not let it bother you that you {s21}. Armies are made to do their leaders' bidding, and hardships are part of a soldier's life."),
  ("npc15_2ary_morality_speech", "You know, friend {playername}, it's none too reassuring to see how you just {s21}. If you can break your word to them, you can break your word to me, is how I figure it."),
  ("npc16_2ary_morality_speech", "Captain -- just so you know, it's no problem by me that we {s21}. We do what we need to do to live, and they'd do the same to us if they were in our shoes."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_2ary_morality_speech", "Galactic Law is not enforced in all planets, but you should still be cautious around populated ones."),
  ("npc18_2ary_morality_speech", "Galactic Law is not enforced in all planets, but you should still be cautious around populated ones."),  
  
  ("npc1_personalityclash_speech", "Captain -- no offense, but I'm a bit tired of {s11}, who puts on airs like she's something better than your humble servant Borcha."),
  ("npc2_personalityclash_speech", "{Sir/Madame} -- as you recall I was a merchant before I signed on with you. I respect men who make their living peacefully, risking all to bring goods for far away lands."),
  ("npc3_personalityclash_speech", "Captain -- in my opinion, {s11} is a hard and cruel man. He speaks of nothing but the need to flog, beat, and hang his fellow soldiers."),
  ("npc4_personalityclash_speech", "{Sir/Madame}. The House of Rolf is one of the most ancient and respected families in this part of the world, with a provenance dating back to the Old Calradic Empire. Yet {s11} openly shows me disrespect, and casts doubt on the provenance of my house."),
  ("npc5_personalityclash_speech", "A moment of your time, captain. {s11} seems to think me a common bandit, just because I have rewarded myself in the past to the legitimate spoils of war from caravans passing through my family's lands."),
  ("npc6_personalityclash_speech", "Your pardon, {sir/madame}, but I cannot keep my tongue stilled any longer. That harlot, {s11} -- every time she sees me she points the five fingers of her hand at me -- a peasant's sign to ward off evil."),
  ("npc7_personalityclash_speech", "Captain, I have done my best to put up with your followers' rude talk and filthy habits. But that one who calls himself {s11} is beyond tolerance."),
  ("npc8_personalityclash_speech", "Just so you know, I cannot abide that insolent mountebank {s11}. Some minutes ago, I was remarking to our companions how the colonists of this region were more than usually slack-jawed and beetle-browed, and speculated that perhaps they had bred with apes."), 
  ("npc9_personalityclash_speech", "Sir -- {s11} is a base braggart, a man with no respect for the honour of women. I am tired of hearing how he conquered this or that damsel."),
  ("npc10_personalityclash_speech", "Excuse me, captain. I hate to trouble you with such things, but I just wanted to let you know that I can't abide that fellow Rolf, the one who calls himself a baron."),
  ("npc11_personalityclash_speech", "Begging your pardon, captain, but I can't keep silent. That man, {s11} -- he killed his own brother."),
  ("npc12_personalityclash_speech", "My lord. The barbarian woman, {s11}, complained of headaches -- a possible symptom of excess of sanguinity. I thought to apply my leeches."),
  ("npc13_personalityclash_speech", "Captain, I weary of {s11}, who talks of nothing but chivalry and feats of arms."),
  ("npc14_personalityclash_speech", "Excuse me, captain. A few minutes ago, I had expressed the opinion that liberal use of the lash and occasional use of the gallows is essential to keep soldiers in line. Men without a healthy fear of their commanders are more likely to run from battle."),
  ("npc15_personalityclash_speech", "Excuse me. I hope you don't mind me telling you that in my opinion, that girl {s11} is a danger to the party. She's a feral brat, disrespectful of authority and the basic principles of the military art."),
  ("npc16_personalityclash_speech", "Oy, captain. Just so you know -- there's something funny about {s11}. He makes strange scrawlings in the dirt, and mutters to himself."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_personalityclash_speech", "Master, a member of your crew just tried to sell me for scrap metal."),
  ("npc18_personalityclash_speech", "Master, a member of your crew just tried to sell me for scrap metal."),  
  
  ("npc1_personalityclash_speech_b", "She's a common bandit, just like myself, and she has no right to tell me to keep my distance from her, as she did just now."),
  ("npc2_personalityclash_speech_b", "I don't much care to hear {s11} gloat about the caravans he has looted, or he plans to loot, like he has no respect for good honest trade."),
  ("npc3_personalityclash_speech_b", "I know that an army is not a nursery, and that strong discipline is important, but I do believe that man enjoys cruelty for cruelty's sake. I hope you do not mind me saying so."),
  ("npc4_personalityclash_speech_b", "{Sir/madame}, these are indeed sorry days if common folk are allowed to mock their betters. That is all."),
  ("npc5_personalityclash_speech_b", "I told him that if the warrior's way bothers him so much, that he become a priest or a beggar and so not have to worry about such things. I hope you do not mind that I said such things."),
  ("npc6_personalityclash_speech_b", "I know the crime I committed was an abomination, but I am seeking repentance, and I deserve better than to be the object of some witch's superstition. I just thought you should know."),
  ("npc7_personalityclash_speech_b", "I do not care for how he stares at me around the campfire after a meal, as he picks his teeth. I believe I recognize him from my days as a bandit. He is base and ignorant. I do not care to travel with such people."),
  ("npc8_personalityclash_speech_b", "{s11}, that font of impudence, overheard me, and called me ignorant, and a savage, and other words I do not care to repeat. It was only out of respect for you that I refrained from cutting his throat then and there. I thought it only fit that I should warn you."),
  ("npc9_personalityclash_speech_b", "If he persists, I shall tell him that he is a base varlot, and if it comes to blows I will not apologize. That is all, {sir/madame}."),
  ("npc10_personalityclash_speech_b", "He's just a simple brigand, as far as I can tell. House of Rolf, my arse. Genuine blue-bloods are bad enough, but those who pretend to be blue-bloods are bloody intolerable. Anyway, I might have said something a bit sharp to him a minute ago. He seemed to take offense, anyway. I just thought you should know."),
  ("npc11_personalityclash_speech_b", "He's a kinslayer, cursed by heaven, and he'll bring misfortune and sorrow upon us, that's for certain. I don't like being around him and I don't think he should be with us. That's all. Sorry for troubling you."),
  ("npc12_personalityclash_speech_b", "But when I tried to afix them, she recoiled and struck me, and accused me of witchcraft. Captain, I am deeply tired of attending to the complaints of such an ungrateful and ignorant lot."),
  ("npc13_personalityclash_speech_b", "Valorous deeds are all very well, but they are not the only goals worth pursuing in life. Personally, I never trust any man who has not at least once woken up drunk in a ditch, or been beaten by the slipper of his lover."),
  ("npc14_personalityclash_speech_b", "That chit {s11} saw fit to admonish me for this. I will not have my methods questioned in front of the men, and I will not serve any commander who tolerates such insubordination in his company. Thank you for allowing me to speak my peace."),
  ("npc15_personalityclash_speech_b", "What's more, I suspect she's a thief. I found her going through my baggage and pawing some of my schematics, and she pulled a knife on me when I thought fit to object. A wise captain would not allow her in his company."),
  ("npc16_personalityclash_speech_b", "Fearing witchcraft, I asked him about it, and he told me that a chit of a girl like myself should mind her own business. So I had a look in his baggage, and found strange plans and diagrams. I think he's a sorceror, {sir/madame}, and if I catch him trying to hex me he'll have a knife in his throat."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_personalityclash_speech_b", "Luckily, the scrap yard said I wasn't worth anything so they brought me back to the ship."),
  ("npc18_personalityclash_speech_b", "Luckily, the scrap yard said I wasn't worth anything so they brought me back to the ship."),  
 
### set off by behavior after victorious battle
  ("npc1_personalityclash2_speech", "Oy -- boss, I don't fancy myself a sensitive soul, but I don't particularly like how {s11} went about cutting the throats of the enemy wounded, back there."),
  ("npc2_personalityclash2_speech", "{Sir/Madame}. If you don't mind, I'd prefer not to be deployed anywhere near {s11}, after what he said to me during that last battle."),
  ("npc3_personalityclash2_speech", "{Sir/Madame}. Since I have joined your company, I have tried hard to learn how to live like a soldier, and how to honour the warrior's code. If I occasionally make mistakes, I would hope to be forgiven."),
  ("npc4_personalityclash2_speech", "{Sir/Madame}. I happened to exchange a few words with {s11} as we were dividing up the spoils of battle. Please inform her that when she speaks to me, she should call me 'Baron' or perhaps 'Baron Rolf,' or 'Your Grace,' but certainly not just 'Rolf.'"),
  ("npc5_personalityclash2_speech", "Captain. {s11} needs to have her tongue cut out."),
  ("npc6_personalityclash2_speech", "My lord. Did you see {s11} during that last battle? He taunts the fallen foe as they lay stricken and helpless on the battlefield, mocking their parentage, their foolishness for having fought us."),
  ("npc7_personalityclash2_speech", "Captain -- I have been searching my mind trying to remember where I have seen {s11}, the one who calls himself a baron. As I watched him in action during that last battle, I suddenly remembered. He is a good fighter, but also a vicious one."), 
  ("npc8_personalityclash2_speech", "Captain. {s11} is a most insolent girl. I have tried to be polite, even friendly, only to have her rebuff me."),
  ("npc9_personalityclash2_speech", "{Sir/My lady}, I hope you do not mind me telling you this, but in my opinion {s11}, the merchant, does not know his place. During that last battle, he cut in front of me to engage a foe whom I had marked for my own."),
  ("npc10_personalityclash2_speech", "{Brother/Sister} -- a question for you. Are you in charge of this company, or is it {s11}?"),
  ("npc11_personalityclash2_speech", "Captain. I don't much care for that {s11}. After that last battle, he went around muttering some heathen incantation, as he went through the slain looking for loot."),
  ("npc12_personalityclash2_speech", "Captain. I can no longer abide the rank ignorance of {s11}. As I was treating the wounded during our last battle, he saw fit to disparage my use of laudanum in relieving the pain while I conducted surgery, and of treating wounds with a poultice of honey."),
  ("npc13_personalityclash2_speech", "Hello, captain! {s11} is a temperamental one, isn't he? During that last battle, I was merely having a friendly chat with our foes about their mothers as we exchanged swordblows, and it caused him to throw a fit!"),
  ("npc14_personalityclash2_speech", "Sir. {s11} is incorrigibly indisciplined. During that skirmish, I called out to him that he should hold ranks with the rest of our battle array. He called back to me that I should 'get stuffed.'"),
  ("npc15_personalityclash2_speech", "Captain -- I must tell you that I question {s11}'s medical credentials. As he was tending to our wounded after that last battle, I saw fit to remind him that the peerless Galerian often advocated administering a distillation of beetroot, to restore the humor imbalance brought by loss of sanguinity."),
  ("npc16_personalityclash2_speech", "Beg your pardon, sir. {s11} might have been a very good thief, but he's not got the stomach to be a warrior, if you ask me."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_personalityclash2_speech", "Master, I've seen some illegal behavior with some members of your crew."),
  ("npc18_personalityclash2_speech", "Master, I've seen some illegal behavior with some members of your crew."),  
  
  ("npc1_personalityclash2_speech_b", "The way she whistles cheerfully as she does it -- it puts a chill down my spine, it does."),#borcha - klethi 
  ("npc2_personalityclash2_speech_b", "The enemy was bearing down on us, and he says, 'Step aside, merchant, this is knight's work.' Next time I will step aside, and let him take a spear in the gut."), #marnid - alayen
  ("npc3_personalityclash2_speech_b", "After our last victory I was picking through the slain, and availed myself of one of our foe's purses. No sooner had I done so then {s11} came up behind me and struck it from my hands, saying that it was she who had made the kill, and thus she deserved the spoils. My lord, I could not tell in the heat of battle who had struck whom. If {s11} had simply told me that she deserved the purse, I would gladly have given it to her."),#Ymira - matheld
  ("npc4_personalityclash2_speech_b", "I am of noble blood, and she is of the basest birth. She must remember her place."),#Rolf - deshavi
  ("npc5_personalityclash2_speech_b", "When the loot was piled up after the last battle, I found among the enemy's baggage a very decent cooking pot. Often I had wished to find such a pot, so I could boil some of the stews that my people use to warm their bellies during the winter months. But {s11} grabs the pot, and tells me that I will not be allowed to 'taint' it with heathen food, and that it should properly belong to her. I yielded the pot to her, but I will not tolerate such disrespect in the future."), #beheshtur- katrin
  ("npc6_personalityclash2_speech_b", "My lord -- such hubris will not be overlooked by Heaven, and I fear we shall all of us pay the price."), #firentis - nizar
  ("npc7_personalityclash2_speech_b", "Back when I lived in the ravines, we would sometimes fight with a rival band called the Brethen of the Woods. Captain -- I would not trust any man who hides his origins, and particularly would not trust a common bandit who calls himself a lord."),#deshavi - rolf
  ("npc8_personalityclash2_speech_b",  "As we were cleaning our weapons after that last battle, I remarked that I thought her a handsome girl, and after I regained my lands I would happily find her a match with one of my warriors. I thought it was a very generous offer, as a woman disinherited by her father is hardly going to find herself awash in prospects. But rather than thank me, she simply turned her back without a word. It was only out of respect for your leadership that I did not immediately try to teach her some manners."),  #matheld - ymira
  ("npc9_personalityclash2_speech_b", "I appreciate that he is willing to risk his life in battle, but that alone does not make a gentleman. He is not of noble birth, and his family's wealth comes from commerce and usury. He may fight with us as an auxiliary, but should not attempt to steal glory from his betters."),# alayen - marnid
  ("npc10_personalityclash2_speech_b", "In that last battle he was shouting at me: 'Go forward, go back, hold the line.' When I told him to mind his own trimming he said he'd have me flogged.  Captain, that man is looking for a crossbow bolt in his chest, begging your pardon."), 
  ("npc11_personalityclash2_speech_b", "He said it was a prayer of thanksgiving for victory, but it didn't sound like that to me. Captain, I don't want him raising up the ghosts of the dead to make trouble for us on our travels. I think you had best be rid of him"),
  ("npc12_personalityclash2_speech_b", "Captain, if that man knew the slightest thing about medical matters, he would know that one should never undermine a patient's confidence in his doctor, particularly not during a complicated operation. If you would be kind enough to dismiss him from this company, you would be doing all of us a great service."), # jeremenus - artimenner
  ("npc13_personalityclash2_speech_b", "When all the dust settled, {s11} turned on me and told me not to 'tempt the wrath of the Heavens' with my 'hubris.' I responded that at least I hadn't killed my own brother, which I think bothers the Heavens a lot more than battlefield small talk. {s11} turns red like a baboon's arse and would have struck me had I not artfully dodged out of his away. Tell him to lighten up, will you?"), #nizar - firentis
  ("npc14_personalityclash2_speech_b", "{Sir/Madame}, such defiance of proper authority is a corrosive influence on our company, and I shall have him flogged if he does so again."), #lazalit - bunduk
  ("npc15_personalityclash2_speech_b", "{s11} responded that Galenian was an 'antiquated know-nothing.' Captain, no true doctor would have such disrespect for the great masters of the past. I do not believe you should employ such an obvious impostor."), #artimenner - jeremus
  ("npc16_personalityclash2_speech_b", "After our last scrap, I was slicing open the guts of some our foes to check for hidden gold, as a girl who counts her pennies ought. He gagged and muttered that I was an 'animal.' I'll inspect his innards for contraband if he doesn't keep a civil tongue in his head."), #klethi - borcha
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_personalityclash2_speech_b", "I just thought you should be aware."),
  ("npc18_personalityclash2_speech_b", "I just thought you should be aware."),  

  ("npc1_personalitymatch_speech", "Boss. {s11} back there didn't do badly in that last fight at all. He's a good egg, too."),
  ("npc2_personalitymatch_speech", "{Sir/Madame}. I just wanted to tell you that {s11} may be a rough sort, and I'll venture a thoroughgoing rogue as well, but I'm proud to call him my companion."),
  ("npc3_personalitymatch_speech", "Hello, {sir/madame}! I had just wanted to tell you that {s11} is a most gallant knight. Did you see him in our last battle?"),
  ("npc4_personalitymatch_speech", "Excuse me, {sir/madame}. I just wanted to say a word in praise of {s11}. He did well in that last battle."),
  ("npc5_personalitymatch_speech", "That was a fine battle, {playername} Bahadur! {s11} is a good man to have by our side in a fight."),
  ("npc6_personalitymatch_speech", "Captain. Sometimes I am troubled by all this bloodshed, although I know that proud warlords must be humbled, and cruel bandits tamed, if we are to restore peace to the Galaxy."),
  ("npc7_personalitymatch_speech", "Captain. I was just talking to {s11}. She may be a bit savage, but I believe that she is a faithful friend."),
  ("npc8_personalitymatch_speech", "A fine battle that was, captain. And I have to say, I admire the taunts that {s11} hurled at our enemy."),
  ("npc9_personalitymatch_speech", "Captain. {s11} acquitted herself well in that fight back there. A fine, modest maiden she is, if I dare say so myself."),
  ("npc10_personalitymatch_speech", "Ahoy, Brother! I wish you joy of your victory! Say, old Mother {s11}'s not bad in a scrap, is she, for a woman of her years? Although I'm getting to be a bit of an old dog myself, now."),
  ("npc11_personalitymatch_speech", "Ach, captain! A fight like that one sets my old joints a-creaking. Still, we licked them pretty good, didn't we?"),
  ("npc12_personalitymatch_speech", "A bloody business, captain, a bloody business -- although a necessary one, of course. {s11}, I believe, shares my ambivalence about this constant fighting."),
  ("npc13_personalitymatch_speech", "You have earned your name today, oh valorous one! And {s11}, too! I like that one. She sings the songs of her people as she goes into battle, which appeals to an artistic soul like my own."),
  ("npc14_personalityclash_speech", "Captain. It is a pleasure going into battle with men like {s11} by my side."),
  ("npc15_personalitymatch_speech", "Captain. I was just having a word with {s11} after our last battle, and it strikes me that the man has got a good head on his shoulders."),
  ("npc16_personalitymatch_speech", "Oy -- captain. I was just having a chat with {s11}, as we picked through the bodies after our last little scrap."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_personalitymatch_speech", "npc17_personalitymatch_speech"),
  ("npc18_personalitymatch_speech", "npc18_personalitymatch_speech"),  
  
  ("npc1_personalitymatch_speech_b", "Without good honest souls like him to bring credits into the Galaxy, scoundrels like me would have a hard time in life, I'll warrant. I'm glad to have him with us."),
  ("npc2_personalitymatch_speech_b", "Based on how he did in that last fight, I'd say that I'd trust my back to him any day, although I'd still keep a hand on my purse."),
  ("npc3_personalitymatch_speech_b", "I also confess that I find him a truly delightful companion, a man of both wit and manners. Perhaps, perhaps... Ah, but I say too much. Good day, {sir/madame}."),
  ("npc4_personalitymatch_speech_b", "You chose well to enlist him in our company. He knows a thing or two about a fight, and also knows the importance of respecting his comrades-in-arms, unlike some others I might mention."),
  ("npc5_personalitymatch_speech_b", "As for his other attributes, I doubt that he is any more a Baron than I am, but I have to admire the brazen way he makes that claim."),
  ("npc6_personalitymatch_speech_b", "I must say that {s11} is a source of great comfort to me. I have told him of my sin, and he said to me that Heaven will forgive my transgression, if I truly repent and truly desire such forgiveness. He is wise, and I am glad that he is with us."),
  ("npc7_personalitymatch_speech_b", "At some point in the future, if you have no need of our services, she has promised to go back to the ravines with me and find the bandits who murdered my lover, and help me take my revenge. It was a kind offer. I am glad that she is with us."),
  ("npc8_personalitymatch_speech_b", "He managed to include their geneology, their appearance, and their eating habits in a well-framed Old Calradic quatrain. I personally prefer the saga, but we Nords respect poetic craftwork when we hear it."),
  ("npc9_personalitymatch_speech_b", "Were she of noble blood, I might ask for her hand. It is a pity that she is a merchant's daughter. But speaking with her is a pleasant way to pass time on the march."),
  ("npc10_personalitymatch_speech_b", "Heh. It just goes to show that youth ain't everything, that experience also wins battles. I reckon she and I could teach the young puppies of the world a thing or two, couldn't we?"),
  ("npc11_personalitymatch_speech_b", "Old {s11} in particular showed them a thing or two, I thought. Not bad for the pair of us, I thought, given that between us we've probably seen close to a hundred winters."),
  ("npc12_personalitymatch_speech_b", "It saddens him deeply to take the lives of his fellow men, however just the cause. He and I have talked together of a brighter future, of the need to unite these petty warring planets, so that we may bring this time of troubles to an end."),
  ("npc13_personalitymatch_speech_b", "Also, although I normally prefer the coy to the Amazonesque, I confess that I have also noticed the femininity she tries to hide beneath her martial demeanour. True, she is a bit aloof on the march and in camp, but perhaps my fair words can melt the Nordic ice around her heart."),
  ("npc14_personalityclash_speech_b", "He is a professional soldier, and though he may not be as fast on his feet as some others, he knows the wisdom of holding together in a disciplined battle-line. You showed good sense in bringing him into this company."),
  ("npc15_personalitymatch_speech_b", "War, like any other affair, requires careful planning and preparation, and a firm grasp of strategic principals. All other things being equal, the best trained army will win the battle, an observation that I think our last fight bears out. The men may curse him now, but they'll learn to thank him, I'll warrant."),
  ("npc16_personalitymatch_speech_b", "Have you heard her story? Can you believe the wrongs done to her? I tell you, it makes my blood boil. I want to cut off all the little bits of those bastards who mistreated her -- and I'll do it, too, if we ever run into them in our travels."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_personalitymatch_speech_b", "npc17_personalitymatch_speech_b"),
  ("npc18_personalitymatch_speech_b", "npc18_personalitymatch_speech_b"),  
  
  ("npc1_retirement_speech", "I'm a bit tired of marching up and down the land, shedding my blood for someone else's cause. The loot is good, but I think I've got enough of that, now. I'm going to head back to my village, take a wife, settle down, maybe raise horses if I can afford it."),
  ("npc2_retirement_speech", "I'm getting a bit tired of the warrior's life. I'm going to invest my share of our loot into a cargo of goods -- furs, linens, velvets, probably -- and take them back over the mountains. I would like to thank you again for taking me on, and wish you the best of luck."),
  ("npc3_retirement_speech", "I am afraid I have something to tell you. I have decided that the warrior's life is not for me. I think it is probably too late for me to find a good marriage -- no one of my people would take a wife who had served with a company of soldiers -- but I may have enough money to start myself up as a merchant. I hope you will not be angry, {sir/madame}."),
  ("npc4_retirement_speech", "I have fought with you honourably, as befits a son of the House of Rolf, but I am not altogether satisfied with your leadership. I will go home to my ancestral estates, which are much in need of my services."),
  ("npc5_retirement_speech", "Bahadur -- since I have taken your salt, I have fought for you fiercely, and loyally. But you have not always repayed my service with the kind of leadership that I deserve. So I am going home, in the hope that the Khan's men have forgotten me, to see my father and brothers again."),
  ("npc6_retirement_speech", "I joined this company in the hope that you would lead me out of darkness, and indeed I have found a measure of peace here. But I have some qualms about your leadership, and have begun to suspect that the path to redemption can be found elsewhere."),
  ("npc7_retirement_speech", "I am tired of this squalid life of endless warfare, seeing men debased by fear, greed, lust, and a hundred other sins. I have money in my purse. I am going overseas to look for a better planet. I assume that you will fare well without me."),
  ("npc8_retirement_speech", "I have fought in your shield wall, and done well by it. But your leadership is not always to my liking, and anyways I have another task. I will take what plunder I have won and raise a warband of my own and sail to Nordland to take back my husband's hall from my treacherous brother-in-law. I wish you well."),
  ("npc9_retirement_speech", "We have fought well together, and earned ourselves much glory. But I have some reservations about your leadership, and at any rate have my patrimony to reclaim. I will be leaving you. Perhaps we will meet again."),
  ("npc10_retirement_speech", "I've had enough of travelling all over this Galaxy. I've got enough to buy a small bit of land somewhere, so I think I'll give that a try. So long, and best of luck to you."),
  ("npc11_retirement_speech", "You did an old woman a great service by taking her into your company. But I'm afraid I'm finding this life no more to my liking than driving a wagon. Too much cold, too much hunger, and at the end all I see in front of me is a hole in the ground. So I'll be off, although I don't know where."),
  ("npc12_retirement_speech", "I've done all right in your company. I filled my belly, put some gold in my purse, and broadened my knowledge of wounds and injury -- I can't complain about that! But I think right now that service in this company is holding me back. I have a duty to share my findings with other surgeons, and for that I need to hire scribes, who are rare in the Galaxy. I shall be going home"),
  ("npc13_retirement_speech", "As the luster of your name grows ever brighter, I fear that my own reputation will seem pale in comparison, as the moon is outshined by the sun. I have decided to strike out on my own. The very best of luck to you!"),
  ("npc14_retirement_speech", "I would like to inform you that I wish to sever our relationship. I intend to seek alternative employment."),
  ("npc15_retirement_speech", "I appreciate that you took me on, but I'm not altogether happy about how things have worked out. I'm going to head off elsewhere -- maybe go home, maybe find another job, I haven't quite decided yet."),
  ("npc16_retirement_speech", "I've had good times in this company, and I've found myself a pretty trinket or two on the battlefield, but right now it isn't working out. I'm leaving you to go offer my talents to someone else."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_retirement_speech", "npc17_retirement_speech"),
  ("npc18_retirement_speech", "npc18_retirement_speech"),  
  
  ("npc1_rehire_speech", "Boss -- it's good to see you again. I know we had our differences in the past, but to tell you the truth, those were some of the best days I've known. And, to tell you the truth, I've had a bit of difficulty finding work. Listen, if you'd be willing to have me back, I'd be willing to sign up with your company again."),
  ("npc2_rehire_speech", "{Sir/Madame}! It's good to see you again. But I'll confess -- I've been looking for you. I bought a load of goods like I told you I would, loaded them up, and took them back across the steppe -- but wouldn't you know it, I was hit again by Khergits, and lost it all. I guess I'm just destined to fight for my fortune. Also, people tell me that you've done very well for yourself. So tell me, {sir/madame}, would you have me back?"),
  ("npc3_rehire_speech", "Well, hello {sir/madame}! It is very good to see you again. I have not fared so well since we parted, I am afraid. My mother's family. whom I hoped would give me a start in trading, have not been as welcoming as I have hoped. I receive nothing but lectures from my aunts, on how I have ruined my prospects for marriage by taking service in a mercenary company. Perhaps I am better suited to war than to commerce, to share a meal over a campfire with rough fellows than to drink wine with the burghers of Veluca. {Sir/Madame}, I must ask you -- will you take me back?"),
  ("npc4_rehire_speech", "Why hello, captain. It's been a while. You've done well for yourself, I hear. For my part, I've been having some difficulties coaxing a living from my estates -- locusts, bad rains, unruly servants, that sort of thing. I thought I might take up the sword once more. I know there's been some bad blood between us, but I'd be honoured to fight in your ranks once again."),
  ("npc5_rehire_speech", "{playername} Bahadur! Your fame grows ever greater -- even as far as my homeland, beyond the mountains. I'd returned there, hoping that the Khan's men had forgotten. Well, they had not -- even before I set foot in my valley, I had word from my family that both the Khan and the Humyan were looking for me. So I came back again, hoping you might forget any harsh words I had spoken, to see if I could fight with you once again."),
  ("npc6_rehire_speech", "It is good to see you, {sir/madame}. Everywhere I go, men are in awe of your deeds. I have not had it so well since I left. Wherever I go, I feel my demons returning. My soul is in turmoil. For reasons that I cannot fully explain, I had found peace in your company, even if I had questions about your leadership. Will you allow me to serve with you once again?"),
  ("npc7_rehire_speech", "Captain! It is good to see you. Forgive what I may have said when we parted. I took a ship out of Wercheg, bound for the east, but it was taken by pirates and after my ransom I was set ashore back here. There may be better places in the world than that planet, but I have yet to see them. So I think, if it is my lot to live here, then your company is as good a livelihood as any. Will you have me back?"),
  ("npc8_rehire_speech", "Greetings to you, {playername}. I was wondering if the harsh words spoken between us in the past could be forgotten. I have been hunting among the Nords here, to see if I could find enough men to take back my husband's hall. But I could not find enough men to crew a longship, and those whom I gathered quickly got bored and wandered off -- not, I will add, before they drank away such gold as I had accumulated. So I thought back to the battles we fought together. Those were good days, and profitable ones too."),
  ("npc9_rehire_speech", "My dear, dear {man/lady}! So good it is to see you! I have sought service with the lords of this land, but have been most grieviously disappointed. Half of them ask me to collect debts from fellow lords, as though I were a banker's errand boy, or chase down his servants, as though I were a farm overseer. One even asked me to murder one of his creditors! I have looked for you, to see if you would wish me to join you again."), #Alayen
  ("npc10_rehire_speech", "Captain! It's good to see you. You see, it turns out I'm not much of a farmer. Too soft on the hired hands, I figure. I let them rob me blind. I guess fighting is what I know best. So tell me, captain, are you still looking for good men?"),
  ("npc11_rehire_speech", "Captain! So good to see you! People say that you've been making gold hand over foot. I'm a fidgety old bag of bones, I'll admit. I left you because I wasn't satisfied with the warrior's life, but I spend a bit of time on planet and I realize that there's worse things in life than a full belly, honest companions, and the joy of seeing the enemy run before you. So, would you be hiring again"),
  ("npc12_rehire_speech", "Captain! It's a fine thing to see an honest face like yours. This world is full of lies. I went home to publish my findings, hired some scribes and made a handful of codices, and waited for the commissions. But it turns out that the universities don't care about real medical knowledge rather than warmed-over Galerian. And publishers -- let me tell you, you never saw anyone so unscrupulous. They rent the books out chapter to by chapter to students to copy, but half of them aren't returned, and those that are have pages soaked in wine, and there's no longer a complete copy of my work anywhere. I'll keep trying, but first I need a bit of money in my pocket, first. Are you looking for a surgeon?"),
  ("npc13_rehire_speech", "Well hello there, oh valorous one. I had been hoping to see you again. Everywhere I go, I hear tales and songs of your deeds. I will admit that I felt a twinge of regret that we had parted ways, and, I'll confess, a twinge of jealousy as well at your reputation. I thought that once again I might fight by your side, and thus bask in the reflection of your glory. Perhaps we might ride together again, for a little while?"),
  ("npc14_rehire_speech", "Captain. It is good to see you. When last we parted, I was ready to swear that I would not serve you again, but perhaps I judged you too harshly. All over the Galaxy, men sing your praises. I have tried serving in other lords' armies, and believe me, what I have seen of them restores my opinion of your leadership. If you would have me in your company, I would fight for you again."),
  ("npc15_rehire_speech", "Why hello, {playername}. I can't say I'm entirely displeased to see you. You see, I took on another contract before I left, and sure enough, when it came time to collect the pay, the lord had nothing but talk and excuses and petty little complaints about my handiwork. I can't say I was always happy in your company, but at least I put gold directly into my purse after every battle. You still offering work?"),
  ("npc16_rehire_speech", "Captain! They say that you've done well for yourself since we last met. I'll come out and admit that I cursed your name when we parted ways, but thinking back on it you weren't all that bad. All these lords, they're glad enough to send me on little side errands, but they don't much care to have me in their main battle-line. Apparently I spook the men. I've heard it muttered that I'm a witch, or that I eat men's hearts after killing them, or other rot. Not that I mind stabbing a man while he's asleep, but it's a lot more gratifying when he's awake and kicking. So I thought I'd try to find you again, see if you'll take me on."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_rehire_speech", "npc17_rehire_speech"),
  ("npc18_rehire_speech", "npc18_rehire_speech"),  
  
#local color strings
  ("npc1_home_intro", "Mandalore. Right up ahead. You'll not find a people more devoted to war."),
  ("npc2_home_intro", "Ah, yes, Mandalore.  An interesting people live there, certainly."),
  ("npc3_home_intro", "Up ahead, that planet Endor.  It's one of the most interesting trading posts you'll ever see."),
  ("npc4_home_intro", "Captain, we're approaching the site of one of my greatest triumphs of piloting."),
  ("npc5_home_intro", "Tatooine.  That's where I got my start, you know."),
  ("npc6_home_intro", "I couldn't help but notice that the sensors show we are approaching Corellia.  If we land, I must stay on the ship."),
  ("npc7_home_intro", "Sernpidal's coming up on the scanner.  That's my homeworld, you know."),
  ("npc8_home_intro", "Watch the scanners.  This is pirate space."),
  ("npc9_home_intro", "Yavin, hm? I hear the Rebels have a base there. They think it's a secret, but I know quite a few things people think are secrets."),
  ("npc10_home_intro", "That's Dathomir, up ahead. A beautiful planet, all the more beautiful when you consider it was the site of one of my greatest battles."),
  ("npc11_home_intro", "Watch for gravitational anomalies, captain, and keep an eye on our six. We're nearing Kessel."),
  ("npc12_home_intro", "Kashyyyk! That's where I'm from! Hey, captain, we're near my home!"),
  ("npc13_home_intro", "Captain, there's something I've been meaning to tell you."),
  ("npc14_home_intro", "Well, captain, there it is. Hoth. The coldest, deadest rock anyone out there calls home."),
  ("npc15_home_intro", "We're nearing Cloud City now. The Bespin system, if you're unfamiliar."),
  ("npc16_home_intro", "Well, we're coming up on Mon Cal, home of the fishheads and the squids.  Of course, they don't much appreciate being called either, but between you and me that's what they are."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_home_intro", "npc17_home_intro"),
  ("npc18_home_intro", "npc18_home_intro"),  

  ("npc1_home_description", "One of their kind, Jango Fett--he was the template for the original clone troopers.  Back in the clone wars, back when you could tell who was a droid and who was a clone and that was that when it came to war.  Things are different now, of course.  Nothing stops an Imperial thug or a Rebel terrorist from painting up his ship with the wrong colors and massacring a settlement to whip up anger at the other side."),
  ("npc2_home_description", "Back when I was a general for the Republic, I had more than a few hired on as mercenaries.  I only hired mercenaries, you know.  I could trust the Mandalorians, because they were clear about what they wanted: glory and a paycheck, and I knew I could give them both.  But their vat-born cousins, the clones...they didn't seem right to me. I refused to employ any of them in my unit. All they wanted was to obey their training, and frankly I don't trust any soldier, flesh or mechanical, who obeys commands other than the ones I pay them to follow."),
  ("npc3_home_description", "Outside the little trader's stop there, it's populated by these tiny, fuzzy things, like a cross between a human and a Kessel rat. My father used to tell me of his days as a trader, when he would stop there to swap bantha meat for the little things' furs.  Oh, I do hope they only took the furs off the ones who were already dead!"),
  ("npc4_home_description", "I was piloting an Action IV bulk freighter through an asteroid belt, when suddenly my warning lights go off left and right, and I look and see that I've got two Z-95s directly on my tail.  See, our escort was scouting far ahead, and the headhunters must have slipped around behind us. Well, I know I'm outgunned badly, but I'm traveling at a good speed, while they're starting from nearly a dead stop.  So I make for this planetoid, right?"),
  ("npc5_home_description", "The Krayt Dragon, they called me.  And while I appreciated all the praises of the Gamorreans I fought, I respected the praises of the Tatooineans more.  It's a harsh planet.  I mean, sure, a Gamorrean boar can punch through a durasteel wall, but they're coddled little things happy to wallow around in pools and fight for fun.  But they have no discipline.  They wouldn't last an hour out in the Tatooine wastes.  Out there in the sands and the burning winds and the glare of the suns, survival is a constant fight."),
  ("npc6_home_description", "You see, I had many friends who also joined up with CorSec, and they all think I'm tragically dead.  I know the odds are low we'd bump into one, but if we did, I'd have to answer some questions I'd rather not.  Don't get me wrong, captain, we're perfectly safe to land, since my ID is clean.  But I haven't changed my face, and I'd rather as few people here see it as possible."),
  ("npc7_home_description", "It's a barren world, poor and rocky. But we're a resilient people. We could withstand just about anything the skies throw at us.  Heh, well, anything but the moon crashing down or something, but what are the odds of something like that happening?  Nah, we've made a nice homeworld there, and so long as the war stays away, I think we'll continue to do just fine."),
  ("npc8_home_description", "The lanes here aren't patrolled, as the result of some border dispute. I can't quite remember the particulars. Most of the pirates here are Duros, though, I know that. I tried learning the craft of bounty hunting under one of them, but I could barely understand a word he said."),
  ("npc9_home_description", "You pick up on these things when your father sells hyperspace drive cores to anyone with the credits. He made trillions doing it. Trillions. He could buy a planet. For all I know, he has. And that should be mine."),
  ("npc10_home_description", "I don't quite remember why I fought there. It was for the Republic, something about a temple, not that I cared. But the battle, captain, the battle! I fought not droids or hired thugs, but witches, hidden in the mires, mounted on great rancors. We were there, my company and I, on the far right of a battle line of two battalions of clones. Suddenly, behind us, we heard trees shattering. We knew they were trying to turn our flank. A hundred Rancors were bearing down on us!"),
  ("npc11_home_description", "Kessel's my home, as much as any place is. I was born there, and there I was a life servant to a spice-lord's son. My father worked in the mines, and my mother tended to the slave children. My job there wasn't the worst by far; the boy often treated me poorly but was not an inhumane sort, and I confess I liked him. He was like a brother and a husband to me, though I had no choice in the matter. I don't know why he sold me. Perhaps he grew tired of me. Perhaps he intended to take a wife, and his chosen didn't understand what I was. I was confused, and I was heartbroken."),
  ("npc12_home_description", "Yeah, only Wooks come from Kashyyyk, I know what you're thinking, and you're right that most of the planet is covered by those big trees and the hairy things that live in 'em.  But no planet's of one type only, captain, just like no nerf is the same color all the way 'round. Up nearer to the poles, the trees are small and hardy grasses grow. And if you don't mind the chill at night, well, I promise you the nerfs won't notice a thing."),
  ("npc13_home_description", "See, I've sold a lot of, er, what I called 'upgrades' to a lot of captains and a lot of mechanics throughout the years. And though I don't remember selling to you, I do recognize my own handiwork when I see it, and, well...I should say that you should probably ease up on the hyperdrive until I can install something a little less, er, shall I say experimental. "),
  ("npc14_home_description", "I trained a company of mercs there a few years back. They went in a bunch of fat, lazy banthas, Five hundred of 'em. Only three hundred of 'em came out, they were a lean, cohesive, and vicious three hundred."),
  ("npc15_home_description", "The only planet of any note in the system is a gas giant, but there's a particularly interesting refinery there. Cloud City, they call it. It's not an economic powerhouse, but its architecture is quite astounding. The city is clearly recently built, for there are some Imperial influences in its edifaces. But yet the tall towers that dot her disc are clearly influenced by traditional Naboo design, and her spires and factory design are neoclassic Alderaan. And yet the whole, from a distance, reminds me of a Mon Cal design."),
  ("npc16_home_description", "I once got hired to hunt a fishhead in Coruscant. That might not sound particularly hard, sure. But before I could get a plan together, he'd hopped a freighter headed back home to this big puddle. Now I do not let prey escape me, captain. I acquired access to a military transport, and I was in Mon Cal before he was. I didn't want him to get in the water, you see, because first there's no shadows or corners to hide me, and second I'm not built for water and fishheads are."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_home_description", "npc17_home_description"),
  ("npc18_home_description", "npc18_home_description"),  
  
  ("npc1_home_description_2", "But the Mandos, they don't go for any of that.  Sure, they'll gladly butcher your family, but they'll make damn sure you know it was them that did it. Since violence is a given nowadays, I can at least respect the honesty."),
  ("npc2_home_description_2", "Most Jedi learned of the Purge when they got a clone's blaster bolt in their back.  But my real, Mandalore-born soldiers stayed loyal to me.  I may not like war, but I can tell you that when it comes, the men and women from that planet are as trustworthy as any you will ever meet."),
  ("npc3_home_description_2", "But now...I feel a very strange presence.  There's something here.  Something terrible, something mechanical...something dark and horrid...but...but...with a flicker of light inside it...no...it's gone.  How strange!  I wonder what that was all about."),
  ("npc4_home_description_2", "By the time I reached the big rock, they were sitting dead on my tail, raking me with fire. All the blown-off bits of scrap metal must have been playing hell with their sensors, though, or maybe they just weren't paying attention to anything but their laser tracking, because when I scraped the armored belly of my ship against that rock, I slowed down right quick...and they didn't. One plowed into my stern, the other veered off at the last second, but lost control and slammed into an asteroid. My freighter was in a bad state, but better than if she was in the hands of pirates."),
  ("npc5_home_description_2", "Fighting isn't something they do for fun, or for honor.  They fight, because that's what Tatooine is. It's a fight, a fight for survival. Everyone there is a veteran of every day they live. I'd put a Tatooine farm boy up against a Gamorrean champion any day. Hell, I'd have spent my whole career in the pits there, if it weren't for the fact that nobody on that sandy rock has two credits to their name."),
  ("npc6_home_description_2", "Corellians are a proud people, with a strong sense of duty. Honorable service is rewarded well, and dereliction of duty...well...let's just say I'll stay on the ship, and that's that."),
  ("npc7_home_description_2", "As for me?  As a young girl, I left to go to Coruscant to study, and there I met my Sothan.  He was just a attendant to the Representative from Fondor then, but I could see the spark of greatness in his eyes...ah, but that was a different time."),
  ("npc8_home_description_2", "I should have known there I wasn't cut out for bounty hunting, but I wasn't about to give up on the family trade so soon. My mum is the best bounty hunter in the Duro system, and I planned on following her. I've got her eye, all right, but it turns out I've got the brains of my dad.  We're not dumb, mind you, but specifics and particulars don't stay in there quite so long as they do with other folk."),
  ("npc9_home_description_2", "Well, let me tell you, it will be mine. Once we're done campaigning together, I'll take what I've learned and what I've earned and raise up a little army of my own. Won't the fat board members be surprised when I burst into one of their little meetings, and dictate terms of my full and complete takeover!"),
  ("npc10_home_description_2", "The first one to come was their war-mother, dressed in paints and shrieking fiercely. Her beast reared back and roared, as she threw a thermal detonator right down at my fireteam. I still don't know how I did it, but I drew a bead and fired clean into her grenade with my pistol. That knocked it back as it detonated, right into the rancor's gullet. That moment, the flash when the bolt hit the detonator, captain, that's why we fight. That's why we live."),
  ("npc11_home_description_2", "I suppose it wasn't a great life I had at Kessel, but it wasn't terrible. I was sheltered from the bitter darkness of the mines, and from the hands of pirates. I was safe and had a warm bed, and my duties were mostly easy and sometimes enjoyable. I did not resent him as you might think I would. While I would rather live a day as a free woman than a century as a slave, for a girl born into slavery, my lot was the best I could have hoped for."),
  ("npc12_home_description_2", "But everybody thinks Kashyyyk is nothing but Wookiees, just because that's the way most of it is. Well, as any nerf-herder knows, if you just trust what most people think about most of something, and assume that mean all of that something is that way, then you've shut off your brains, and frankly, you're even dumber than a nerf.  That's what I think, anyway."),
  ("npc13_home_description_2", "Don't worry, though, captain.  We're not at any risk or anything.  I'm sure that it's completely harmless. But...just do be safe, okay?  I promise I'll remove it as soon as we land next, and put everything right again."),
  ("npc14_home_description_2", "Harsh climates like those, they send the cowards and weaklings who have no business anywhere near an army running back for the safety of home. If you ever find yourself needing to turn a rabble into an army, then that windswept rock of ice and snow is the best place I can think of."),
  ("npc15_home_description_2", "It's well worth a visit if you have an interest in architecture, captain. I've not found a more interesting city in the galaxy."),
  ("npc16_home_description_2", "After I disembarked, I checked the docking schedules and found I was two hours ahead of schedule. Happily, I learned his spawnling would be there to greet him. I tracked it down, and making like I accidentally bumped into the tot, I affixed a very small, poisoned needle to its forehead. Imperceptible, but very sharp. One paternal hug later, the job was done. It was beautiful, captain, and I don't like to praise my own work."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_home_description_2", "npc17_home_description_2"),
  ("npc18_home_description_2", "npc18_home_description_2"),  
  
  ("npc1_home_recap", "I was an Imperial.  Then I found some things I didn't want to find, and I realized I'm the only one worth looking out for."),
  ("npc2_home_recap", "I'd rather keep most of it to myself, to be honest."),
  ("npc3_home_recap", "I'm the daughter of a merchant, but that's not very exciting at all."),
  ("npc4_home_recap", "I'm from Coruscant, and I spent my youth in the flight simulators."),
  ("npc5_home_recap", "I was born on Manaan, learned to fight on Tatooine, and spent most of my career on Gamorr."),
  ("npc6_home_recap", "I'm a Corellian, pure-blooded and proud of it."),
  ("npc7_home_recap", "I could have sworn I told you this already."),
  ("npc8_home_recap", "I'm from Duro. I don't quite remember how my family got there, but they're there regardless."),
  ("npc9_home_recap", "My story is as engrossing as any you'll hear in a holovid, full of triumph and betrayal."),
  ("npc10_home_recap", "Born on Mandolore. Trained on Mandolore. Don't know where I'll die, but I know it will be in glory."),
  ("npc11_home_recap", "Mine is not a happy story, captain, though you are providing me a better ending than I could have hoped for."),
  ("npc12_home_recap", "Born on Kashyyyk, I was, but the first time I ever saw a Wookiee was after I left. I thought they were just some joke my daddy made up to scare me."),
  ("npc13_home_recap", "I've traveled from as far back as I can remember. I don't even know where I was born, to be honest."),
  ("npc14_home_recap", "I've fought in a hundred battles myself, and I've trained men who fought in a thousand more."),
  ("npc15_home_recap", "I'm from over the hills. But travelling the Galaxy is where the money is to be made, these days, if your trade is siegecraft."),
  ("npc16_home_recap", "Captain, the less you know about me, the better, I promise you."),
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_home_recap", "I am a robot."),
  ("npc18_home_recap", "I am a robot."),  
  
  ("npc1_honorific", "boss"), #Borcha
  ("npc2_honorific", "{sir/sir}"), #marnid
  ("npc3_honorific", "{sir/sir}"),
  ("npc4_honorific", "{sir/sir}"),
  ("npc5_honorific", "{playername}"), #beheshtur
  ("npc6_honorific", "captain"), #firentis
  ("npc7_honorific", "captain"), #deshavi
  ("npc8_honorific", "{playername}"), #matheld
  ("npc9_honorific", "{sir/sir}"), #Alayen
  ("npc10_honorific", "boss"), #Bunduk
  ("npc11_honorific", "{sir/sir} -- I mean Captain"), #katrin
  ("npc12_honorific", "captain"),
  ("npc13_honorific", "captain"), #nizar
  ("npc14_honorific", "captain"), #lazalit
  ("npc15_honorific", "captain"), #artimenner
  ("npc16_honorific", "captain"), #klethi
  #SW - new droid NPC's (copied personlity from npc6)
  ("npc17_honorific", "master"),
  ("npc18_honorific", "master"),  

#NPC companion changes end

#Troop Commentaries begin
#Tags for comments are = allied/enemy, friendly/unfriendly, and then those related to specific reputations
#Also, there are four other tags which refer to groups of two or more reputations (spiteful, benevolent, chivalrous, and coldblooded)
#The game will select the first comment in each block which meets all the tag requirements

#Beginning of game comments
("comment_intro_liege_affiliated", "I am told that you are pledged to one of the pretenders who disputes my claim. But we may still talk."),

("comment_intro_famous_liege", "Your fame runs before you! Perhaps it is time that you sought a liege worthy of your valor."),
("comment_intro_famous_martial", "Your fame runs before you! Perhaps we shall test each other's valor in a tournament, or on the battlefield!"),
("comment_intro_famous_badtempered", "I've heard of you. Well, I'm not one for bandying words, so if you have anything to say, out with it."),
("comment_intro_famous_pitiless", "I know your name. It strikes fear in men's hearts. That is good. Perhaps we should speak together, some time."),
("comment_intro_famous_cunning", "Ah, yes. At last we meet. You sound like a good {man/woman} to know. Let us speak together, from time to time."),
("comment_intro_famous_sadistic", "I know your name -- and from what I hear, I'll warrant that many a grieving widow knows too. But that is no concern of mine."),
("comment_intro_famous_goodnatured", "I've heard of you! It's very good to finally make your acquaintance."),
("comment_intro_famous_upstanding", "I know your name. They say you are a most valiant warrior. I can only hope that your honour and mercy matches your valor."),

("comment_intro_noble_liege", "I see that you carry a nobleman's banner, although I do not recognize the device. Know that I am always looking for good men to fight for me, once they prove themselves to be worthy of my trust."),
("comment_intro_noble_martial", "I see that you carry a nobleman's banner, but I do not recognize the device. Perhaps one day we shall test each other's valor in a tournament, or on the battlefield!"),
("comment_intro_noble_badtempered", "I don't recognize the device on your banner. No doubt another foreigner come to our lands, as if we didn't have so many here already."),
("comment_intro_noble_pitiless", "I see that you carry a nobleman's banner, but I do not recognize the device. Another vulture come to grow fat on the leftovers of war, no doubt!"),
("comment_intro_noble_cunning", "I see that you carry a nobleman's banner, but I do not recognize the device. Still, it is always worthwhile to make the acquaintance of {men/women} who may one day prove themselves to be great warriors."),
("comment_intro_noble_sadistic", "I see that you carry a nobleman's banner, but I do not recognize the device. Perhaps you are the bastard {son/daughter} of a puffed-up nerf herder? Or perhaps you stole it?"),
("comment_intro_noble_goodnatured", "I see that you carry a nobleman's banner, but I do not recognize the device. Forgive my ignorance, {sir/madame}! It is good to make your acquaitance."),
("comment_intro_noble_upstanding", "I see that you carry a nobleman's banner, but I do not recognize the device. No doubt you have come to this planet in search of wealth and glory. If this indeed is the case, then I only ask that you show mercy to those poor souls caught in the path of war."),

("comment_intro_common_liege", "You may be of common birth, but know that I am always looking for good men to fight for me, if they can prove themselves to be worthy of my trust."),
("comment_intro_common_martial", "Perhaps you are not of gentle birth, but if you prove yourself a {man/woman} of valor, then I would be pleased to try my strength against yours in the tournament or on the battlefield."),
("comment_intro_common_badtempered", "Speak quickly, if you have anything to say, for I have no time to be bandying words with common soldiers of fortune."),
("comment_intro_common_pitiless", "You have the look of a mercenary, another vulture come to grow fat on the misery of this land."),
("comment_intro_common_cunning", "Well... I have not heard of you, but you have the look of a {man/woman} who might make something of {himself/herself}, some day."),
("comment_intro_common_sadistic", "Normally I cut the throats of impudent commoners who barge into my presence uninvited, but I am in a good mood today."),
("comment_intro_common_goodnatured", "Well, you look like a good enough sort."),
("comment_intro_common_upstanding", "Peace to you, and always remember to temper your valor with mercy, your courage with honour."),


#Actions vis-a-vis civilians
  ("comment_you_raided_my_minorplanet_enemy_benevolent",    "You have attacked innocent farmers under my protection on the planet of {s51}.  I will punish you for your misdeeds!"), 
  ("comment_you_raided_my_minorplanet_enemy_spiteful",      "You have raided the planet of {s51}, destroying my property and killing some citizens. I will take my compensation in blood!"), 
  ("comment_you_raided_my_minorplanet_enemy_coldblooded",   "You have raided the planet of {s51}, destroying my property and killing some citizens. I will make you think twice before you disrupt my revenues like that again."), 
  ("comment_you_raided_my_minorplanet_enemy",               "You have raided the planet of {s51}, destroying my property and killing citizens under my protection. You will pay the price for your crime!"), 
  ("comment_you_raided_my_minorplanet_unfriendly_spiteful", "You have raided the planet of {s51}. Do it again and I'll gut you like a tauntaun."),
  ("comment_you_raided_my_minorplanet_friendly",            "You have raided the planet of {s51}. This will place a grave strain on our friendship."),
  ("comment_you_raided_my_minorplanet_default",             "You have raided the planet of {s51}. If you continue to behave this way, we will become enemies."),

  ("comment_you_robbed_my_minorplanet_enemy_coldblooded", "You have robbed the citizens on the planet of {s51}. I take that as a personal insult."), 
  ("comment_you_robbed_my_minorplanet_enemy",             "You have robbed innocent farmers under my protection on the planet of {s51}.  I will punish you for your misdeeds!"), 
  ("comment_you_robbed_my_minorplanet_friendly_spiteful", "I have heard that you stole some food from the citizens on {s51}. Well, I'll not fight you over a scrap or two, but keep in mind that I'm the one who must listen to their complaining afterward."),
  ("comment_you_robbed_my_minorplanet_friendly",          "I have heard that you requisitioned supplies from the citizens on {s51}. I am sure that you would not have done so were you not desperately in need."),
  ("comment_you_robbed_my_minorplanet_default",           "You have robbed the citizens on the planet of {s51}. If you continue to behave this way, we may soon become enemies."),

  ("comment_you_accosted_my_caravan_enemy",          "You have been attacking caravans under my protection. But your trail of thievery will soon come to an end."),
  ("comment_you_accosted_my_caravan_default",        "You have been attacking caravans under my protection. This sort of behavior must stop."),

  ("comment_you_helped_villagers_benevolent",                "I heard that you gave assistance to the citizens on the planet of {s51}. I had been neglectful in my duties as commander, and I appreciate what you have done."),
  ("comment_you_helped_villagers_friendly_cruel",            "I heard that you gave assistance to the citizens on the planet of {s51}. I appreciate that you meant well, but I'd rather you not undercut my authority like that."),
  ("comment_you_helped_villagers_friendly",                  "I heard that you gave assistance to the citizens on the planet of {s51}. Times are hard, and I know that you mean well, so I will not object to you providing them with assistance."),
  ("comment_you_helped_villagers_unfriendly_spiteful",       "I heard that you gave assistance to the citizens on the planet of {s51}. As amusing as it is to see you grubbing for favor among my commanders, I would ask you to mind your own business."),
  ("comment_you_helped_villagers_cruel",                     "I heard that you gave assistance to the citizens on the planet of {s51}. As the citizens commander, it is most properly my duty to assist them in times of hardship. You may mean well, but your actions still undercut my authority. I would thank you to leave them alone."),
  ("comment_you_helped_villagers_default",                   "I heard that you gave assistance to the citizens on the planet of {s51}. Times are hard, and I know that you mean well, but try not to make a habit of it. I am their commander, and I would rather not have them go looking to strangers for assistance."),


#Combat-related events


  ("comment_you_captured_a_spacestation_allied_friendly",            "I heard that you have besieged and taken {s51}. That was a great victory, and I am proud to call you my friend!"), 
  ("comment_you_captured_a_spacestation_allied_spiteful",            "I heard that you have besieged and taken {s51}. Good work! Soon, we will have all their resources, their credits, and servants to serve us our wine."), 
  ("comment_you_captured_a_spacestation_allied_unfriendly_spiteful", "I heard that you have besieged and taken {s51}. Well, I guess you got lucky. Enjoy it while you can, until another commander destroys you like I expect they will."), 
  ("comment_you_captured_a_spacestation_allied_unfriendly",          "I heard that you have besieged and taken {s51}. Whatever our differences in the past, I must offer you my congratulations."), 
  ("comment_you_captured_a_spacestation_allied",                     "I heard that you have besieged and taken {s51}. We have them on the run!"), 

  ("comment_you_captured_my_spacestation_enemy_spiteful",            "I hear that you have broken into my home at {s51}. I hope the prison is to your liking, as you will be spending much time there in the years to come."),
  ("comment_you_captured_my_spacestation_enemy_chivalrous",          "You hold {s51}, my rightful planet. I hope you will give me the chance to win it back!"),
  ("comment_you_captured_my_spacestation_enemy",                     "You have something that belongs to me -- {s51}. I will make you return it."),

###Add some variation to these
  ("comment_we_defeated_a_lord_unfriendly_spiteful",           "I suppose you will want to drink to the memory of our victory over {s54}. Well, save your wine -- it will take more than that to wipe out the stain of your earlier disgraces."), 
  ("comment_we_defeated_a_lord_unfriendly",                    "I will not forget how we fought together against {s54}, but I can also not forget the other matters that lie between us."), 
  ("comment_we_defeated_a_lord_cruel",                         "That was a great victory over {s54}, wasn't it? We destroyed his army with ease!"), 
  ("comment_we_defeated_a_lord_quarrelsome",                   "I won't forget how we destroyed {s54}? I enjoyed that."), 
  ("comment_we_defeated_a_lord_upstanding",                    "I will not forget our victory over {s54}. Let us once again give thanks to our leader and allies."), 
  ("comment_we_defeated_a_lord_default",                       "That was a great victory over {s54}, wasn't it? I am honored to have fought by your side."), 

  ("comment_we_fought_in_siege_unfriendly_spiteful",           "I suppose you will want to drink to the memory of our capture of {s51}. Well, save your wine -- it will take more than that to wipe out the stain of your earlier disgraces."), 
  ("comment_we_fought_in_siege_unfriendly",                    "I will not forget how we together we stormed {s51}, but I can also not forget the other matters that lie between us."), 
  ("comment_we_fought_in_siege_cruel",                         "I won't forget how we broke through the walls of {s51} and put its defenders to the sword. It is a sweet memory."), 
  ("comment_we_fought_in_siege_quarrelsome",                   "Remember how the enemy squealed when we came over the walls of {s51}? They had thought they were safe! We wiped the smug smiles of their faces!"), 
  ("comment_we_fought_in_siege_upstanding",                    "I will not forget our capture of {s51}. Let us once again give thanks to heaven, and pray that we not grow too proud."), 
  ("comment_we_fought_in_siege_default",                       "I will not forget how together we captured {s51}. I am honoured to have fought by your side."), 

  ("comment_we_fought_in_major_battle_unfriendly_spiteful",    "I suppose you will want to drink to the memory of our great victory near {s51}. Well, save your wine -- it will take more than that to wipe out the stain of your earlier disgraces."), 
  ("comment_we_fought_in_major_battle_unfriendly",             "I will not forget how we fought together in the great battle near {s51}, but I can also not forget the other matters that lie between us."), 
  ("comment_we_fought_in_major_battle_cruel",                  "I won't forget the great battle near {s51}, when we broke through the enemy lines and they ran screaming before us. It is a sweet memory."), 
  ("comment_we_fought_in_major_battle_quarrelsome",            "That was a fine fight near {s51}, when we made those bastards run!"), 
  ("comment_we_fought_in_major_battle_upstanding",             "I will not forget how we fought side by side at the great battle near {s51}. Let us once again give thanks to heaven, and pray that we not grow too proud."), 
  ("comment_we_fought_in_major_battle_default",                "I will not forget how we fought side by side at the great battle near {s51}. I am honoured to have fought by your side."), 




  ("comment_you_defeated_a_lord_allied_liege",                   "So, you crossed swords with that rascal they call {s54}, and emerged victorious. I am very happy to hear that."), 
  ("comment_you_defeated_a_lord_allied_unfriendly_spiteful",     "I heard that you fought and defeated {s54}. Every dog has its day, I suppose."), 
  ("comment_you_defeated_a_lord_allied_spiteful",                "I heard that you fought and defeated that dog {s54}. Ah, if only I could have heard him whimpering for mercy."), 
  ("comment_you_defeated_a_lord_allied_unfriendly_chivalrous",   "I heard that you fought and defeated {s54}. I hope that you did not use dishonourable means to do so."),
  ("comment_you_defeated_a_lord_allied",                         "I heard that you fought and defeated {s54}. I wish you joy of your victory."), 

  ("comment_you_defeated_me_enemy_chivalrous", "I will not begrudge you your victory the last time that we met, but I am anxious for another round!"), 
  ("comment_you_defeated_me_enemy_spiteful",   "I have been looking forward to meeting you again. Your tricks will not deceive me a second time, and I will relish hearing your cries for mercy."), 
  ("comment_you_defeated_me_enemy",            "When last we met, {playername}, you had the better of me. But I assure you that it will not happen again!"), 

  ("comment_I_defeated_you_enemy_spiteful",          "Back for more? Make me fight you again, and I'll feed your bowels to my hounds."), 
  ("comment_I_defeated_you_enemy_chivalrous",        "Come to test your valor against me again, {playername}?"), 
  ("comment_I_defeated_you_enemy_benevolent",        "So once again you come at me? Will you ever learn?"), 
  ("comment_I_defeated_you_enemy_coldblooded",       "You are persistent, but a nuisance."),
  ("comment_I_defeated_you_enemy",                   "How many times must I chastise you before you learn to keep your distance?"), 


  ("comment_we_were_defeated_unfriendly_spiteful",   "Last I saw you, you had been struck down by the men of {s54}. I blame you for that disaster. What a pity to see that you survived."), 
  ("comment_we_were_defeated_unfriendly",            "Last I saw you, you had been struck down by the men of {s54}. Well, I see that you survived."), 
  ("comment_we_were_defeated_cruel",                 "Last I saw you, you had been struck down by the men of {s54}. Don't worry -- we'll find him, and make him choke on his victory."), 
  ("comment_we_were_defeated_default",               "Last I saw you, you had been struck down by the men of {s54}. It is good to see you alive and well."), 

  ("comment_you_were_defeated_allied_friendly_spiteful",      "I heard that {s54} gave you a hard time. Don't worry, friend -- I'll find him for you, and make you a gift of his head."), 
  ("comment_you_were_defeated_allied_unfriendly_cruel",       "I had heard that {s54} slaughtered your men like sheep. But here you are, alive. Such a disappointment!"), 
  ("comment_you_were_defeated_allied_spiteful",               "I heard that {s54} crushed you underfoot like an ant. Hah! Children should not play games made for grown-ups, little {boy/girl}!"), 
  ("comment_you_were_defeated_allied_pitiless",               "I heard that {s54} defeated you, and scattered your forces. That is most disappointing..."), 
  ("comment_you_were_defeated_allied_unfriendly_upstanding",  "I heard that {s54} defeated you. Perhaps you should consider if you have considered any misdeeds, that might cause heaven to rebuke you in this way."), 
  ("comment_you_were_defeated_allied_unfriendly",             "I heard that {s54} defeated you. Look, try not to get too many of our men killed, will you?"), 
  ("comment_you_were_defeated_allied",                        "I heard that {s54} defeated you. But take heart -- the tables will soon be turned!"), 

  ("comment_you_helped_my_ally_unfriendly_chivalrous",        "I heard that you saved {s54} from likely defeat. Whatever else I may think of you, I must at least commend you for that."), 
  ("comment_you_helped_my_ally_unfriendly",                   "[revelance should be zero, and this message should not appear]"), 
  ("comment_you_helped_my_ally_liege",                        "I heard that you saved my commander {s54} from likely defeat. "), 
  ("comment_you_helped_my_ally_unfriendly_spiteful",          "I heard that you rode to the rescue of our poor {s54}. Did you think him a damsel in distress? No matter -- it's a common mistake."), 
  ("comment_you_helped_my_ally_spiteful",                     "I heard that you saved {s54} from a whipping. You should have let him learn his lesson, in my opinion."), 
  ("comment_you_helped_my_ally_chivalrous",                   "I heard that you got {s54} out of a tight spot. That was a noble deed."), 
  ("comment_you_helped_my_ally_default",                   "I heard that you got {s54} out of a tight spot. Good work!"), 
 
  ("comment_you_were_defeated_allied_unfriendly",             "I heard that {s54} defeated you. Look, try not to get too many of our men killed, will you?"), 
  ("comment_you_were_defeated_allied",                        "I heard that {s54} defeated you. But take heart -- the tables will soon be turned!"), 

  ("comment_you_abandoned_us_unfriendly_spiteful",     "You worm! You left us alone to face {s54}, didn't you? I spit at you."), 
  ("comment_you_abandoned_us_unfriendly_pitiless",     "Well... You abandoned me in the middle of a battle with {s54}, didn't you? I'll see you buried in a traitor's grave."), 
  ("comment_you_abandoned_us_spiteful",                "You disappeared in the middle of that battle with {s54}... I hope you have a good explanation. Did your bowels give out? Were you shaking too hard with fear to hold your weapon?"), 
  ("comment_you_abandoned_us_chivalrous",              "What happened? You disappeared in the middle of that battle against {s54}. I can only hope that you were too badly wounded to stand, for I would be ashamed to have gone into battle alongside a coward."), 
  ("comment_you_abandoned_us_benefitofdoubt",          "What happened? You disappeared in the middle of that battle against {s54}. I assume that you must have been wounded, but it did look suspicious."), 
  ("comment_you_abandoned_us_default",                 "What happened? One moment you were fighting with us against {s54}, the next moment you were nowhere to be found?"), 

  ("comment_you_ran_from_me_enemy_spiteful",          "Last time we met, you ran from me like a whipped dog. Have you come back to bark at me again, or to whine for mercy?"), 
  ("comment_you_ran_from_me_enemy_chivalrous",        "Last time we met, you fled from me. Learn to stand and fight like a gentleman!"), 
  ("comment_you_ran_from_me_enemy_benevolent",        "When I saw you flee the last time that we met, I had hoped that I would not have to fight you again."), 
  ("comment_you_ran_from_me_enemy_coldblooded",       "Last time we met, you fled from me. That was a wise decision"),
  ("comment_you_ran_from_me_enemy",                   "You may have been able to escape the last time we crossed paths, but the next time I doubt that you be so lucky."), 

  ("comment_you_ran_from_foe_allied_chivalrous",      "They say that you fled from {s54}, leaving your men behind. I pray that this is not true, for such conduct does dishonour to us all."), 
  ("comment_you_ran_from_foe_allied_upstanding",      "They say that you fled from {s54}, leaving your men behind. I do not always believe such rumors, and I also know that desperate straits call for desperate measures. But I beg you to take more care of your good name, for men will not fight in our armies if they hear that we abandon them on the field of battle."), 
  ("comment_you_ran_from_foe_allied_spiteful",        "By the way, they said that you ran away from {s54} like a quaking little rabbit, leaving your men behind to be butchered. Ha! What a sight that would have been to see!"), 


  ("comment_you_defeated_my_friend_enemy_pragmatic",  "You may have bested {s54}, but you cannot defeat us all."), 
  ("comment_you_defeated_my_friend_enemy_chivalrous", "I have heard that you defeated {s54}, and ever since have been anxious to cross swords with you."), 
  ("comment_you_defeated_my_friend_enemy_spiteful",   "Your fame runs before you, {playername}. {s54} may have fallen for your tricks, but if you fight me, you'll find a me a much more slippery foe."), 
  ("comment_you_defeated_my_friend_enemy",            "They say that you have defeated {s54}. But I will be a truer test of your skill at arms."), 

  ("comment_you_captured_a_lord_allied_friendly_spiteful",   "I heard that you captured {s54}. I hope that you squeezed him for every credit."), 
  ("comment_you_captured_a_lord_allied_unfriendly_spiteful", "I heard that you captured {s54}. Your coffers must be well-bloated with ransom by now. Such a pity that money cannot transform a low-born cur into a gentleman!"), 
  ("comment_you_captured_a_lord_allied_chivalrous",          "I heard that you captured {s54}. Well done. I assume, of course, that he has been been treated with the honours due his rank."), 
  ("comment_you_captured_a_lord_allied",                     "I heard that you captured {s54}. Well done. His ransom must be worth quite something."), 

  ("comment_you_let_go_a_lord_allied_chivalrous",            "I heard that you captured {s54}, but then let him go. Such chivalry does a credit to our cause."),
  ("comment_you_let_go_a_lord_allied_upstanding",            "I heard that you captured {s54}, but then let him go. Well, that was an honourable course of action, if possibly also a dangerous one."),
  ("comment_you_let_go_a_lord_allied_coldblooded",           "I heard that you captured {s54}, but then let him go. That was most chivalrous of you, but chivalry does not win wars."),
  ("comment_you_let_go_a_lord_allied_unfriendly_spiteful",   "I heard that you captured {s54}, but then let him go. How very chivalrous of you! No doubt the widows and orphans he leaves in his wake will want to commend you in person."),
  ("comment_you_let_go_a_lord_allied",                       "I heard that you captured {s54}, but then let him go. Well, I will not tell you what to do with your own prisoners."),


  ("comment_you_let_me_go_spiteful",                    "When last we met, you had me at your mercy and allowed me to go free. I hope you enjoyed toying with me, like a cat with a mouse, because soon I will have you at my mercy, to slay or humiliate according to my fancy."),
  ("comment_you_let_me_go_enemy_chivalrous",            "When last we met, you had me at your mercy and allowed me to go free. That was most chivalrous of you, and I will not forget. But I also must remember my oath to my liege, and our factions are still at war."),
  ("comment_you_let_me_go_enemy_coldblooded",           "When last we met, you had me at your mercy and allowed me to go free. But we are still enemies, and I cannot promise to repay your mercy in kind."),
  ("comment_you_let_me_go_enemy",                       "When last we met, you had me at your mercy and allowed me to go free. That was kind of you. But we are still at war."),
  ("comment_you_let_me_go_default",                     "When last we met, you had me at your mercy and allowed me to go free. That was kind of you, and I am glad that our factions are no longer at war."),


#Internal faction events
  ("comment_pledged_allegiance_allied_martial_unfriendly",             "I heard that you have pledged allegiance to our leader, {s54}. Pray do not disgrace us by behaving in a cowardly fashion."),
  ("comment_pledged_allegiance_allied_martial",                        "I heard that you have pledged allegiance to our leader, {s54}. I look forward to fighting alongside you against our foes."),
  ("comment_pledged_allegiance_allied_quarrelsome_unfriendly",         "I heard that you have pledged allegiance to our leader, {s54}. Bah. Do yourself a favor, and stay out of my way."),
  ("comment_pledged_allegiance_allied_quarrelsome",                    "I heard that you have pledged allegiance to our leader, {s54}. Fight hard against our foes, respect your betters, and don't cross me, and we'll get along fine."),
  ("comment_pledged_allegiance_allied_selfrighteous_unfriendly",       "I heard that you have pledged allegiance to our leader, {s54}. If I were he, I would not trust you to clean the sculleries."),
  ("comment_pledged_allegiance_allied_selfrighteous",                  "I heard that you have pledged allegiance to our leader, {s54}. Fight bravely and you will be well-rewarded. Betray us, and we shall make of you the kind of example that will not soon be forgotten."),
  ("comment_pledged_allegiance_allied_cunning_unfriendly",             "I heard that you have pledged allegiance to our leader, {s54}. I do not pretend to be happy about his decision, but perhaps it is better to have you inside our tent pissing out, than the other way around."),
  ("comment_pledged_allegiance_allied_cunning",                        "I heard that you have pledged allegiance to our leader, {s54}. That is good. The more skilled fighters we have with us in these troubled times, the better. I shall be watching your progress."),
  ("comment_pledged_allegiance_allied_debauched_unfriendly",           "I heard that you have pledged allegiance to our leader, {s54}. No doubt you will soon betray him, and I will have the pleasure of watching you die a traitor's death."),
  ("comment_pledged_allegiance_allied_debauched",                      "I heard that you have pledged allegiance to our leader, {s54}. Excellent... I am sure that you and I will become very good friends. But remember -- if you betray us, it will be the biggest mistake you will ever make."),
  ("comment_pledged_allegiance_allied_goodnatured_unfriendly",         "I heard that you have pledged allegiance to our leader, {s54}. Well, I can't say that I would have trusted you, but perhaps you deserve the benefit of the doubt."),
  ("comment_pledged_allegiance_allied_goodnatured",                    "I heard that you have pledged allegiance to our leader, {s54}. Good {man/woman}! Our leader is a intellegent commander, and rewards loyalty and valor with kindness and generosity."),
  ("comment_pledged_allegiance_allied_upstanding_unfriendly",          "I heard that you have pledged allegiance to our leader, {s54}. Alas, from what I know of you I fear that you will disgrace us, but I will be happy if you prove me wrong."),
  ("comment_pledged_allegiance_allied_upstanding",                     "I heard that you have pledged allegiance to our leader, {s54}. Fight against our foes with valor, but also with honour and compassion. A good name is as valuable as a sharp sword or a swift speeder in affairs of arms."),


  ("comment_our_king_granted_you_a_fief_allied_friendly_cruel",     "I heard that {s54} granted you {s51} as a planet. Don't forget -- spare the whip and spoil the peasant!"),
  ("comment_our_king_granted_you_a_fief_allied_friendly_cynical",   "I heard that {s54} granted you {s51} as a planet. I am glad to see you prosper -- but be careful. Men are vipers, envious and covetous of their neighbours' wealth. Stay close to me, and I'll watch your back."),

  ("comment_our_king_granted_you_a_fief_allied_friendly",              "I heard that {s54} granted you {s51} as a planet. May your new lands prosper."),
  ("comment_our_king_granted_you_a_fief_allied_unfriendly_upstanding", "I heard that {s54} granted you {s51} as a planet. But keep in mind that pride goes before a fall."),
  ("comment_our_king_granted_you_a_fief_allied_unfriendly_spiteful",   "I heard that {s54} granted you {s51} as a planet. I suspect, however, that fortune is only raising you up so as to humble you even more, when it casts you back into the dung from whence you came."),
  ("comment_our_king_granted_you_a_fief_allied_spiteful",              "I heard that {s54} granted you {s51} as a planet. Let's hope you are indeed deserving of our leader's favor."),

  ("comment_our_king_granted_you_a_fief_allied",                       "I heard that {s54} granted you {s51} as a planet. You seem to be doing very well for yourself."),

  ("comment_you_renounced_your_alliegance_enemy_friendly",             "I heard that you renounced your allegiance to our leader, {s54}. It grieves me that we must now meet on the field of battle."),
  ("comment_you_renounced_your_alliegance_friendly",                   "I heard that you renounced your allegiance to our leader, {s54}. Let us pray that we may not come to blows."),
  ("comment_you_renounced_your_alliegance_unfriendly_spiteful",        "I always had you figured for a traitor to {s54}, and now it seems I was proven right. I hope you are prepared to die a traitor's death!"),
  ("comment_you_renounced_your_alliegance_unfriendly_moralizing",      "I heard that you renounced your allegiance to our leader, {s54}. I am forced to consider you a traitor."),
  ("comment_you_renounced_your_alliegance_enemy",                      "I heard that you renounced your allegiance to our leader, {s54}. Well, it is the way of the world for old comrades to become enemies."),
  ("comment_you_renounced_your_alliegance_default",                    "I heard that you renounced your allegiance to our leader, {s54}. Well, that is your decision, but do not expect me to go easy on you when we meet on the battlefield."),


  ("personality_archetypes",   "leader"),
  ("martial",                  "martial"),
  ("quarrelsome",              "bad-tempered"),
  ("selfrighteous",            "pitiless"),
  ("cunning",                  "cunning"),
  ("debauched",                "sadistic"),
  ("goodnatured",              "good-natured"),
  ("upstanding",               "upstanding"),

  ("surrender_demand_default",        "Yield or die!"),
  ("surrender_demand_martial",        "The odds are not in your favor today. You may fight us, but there is also no shame if you yield now."),
  ("surrender_demand_quarrelsome",    "I've got you cornered. Give up, or I'll ride you down like a dog."),
  ("surrender_demand_pitiless",       "You cannot defeat me, and I'll teach you a painful lesson if you try. Yield!"),
  ("surrender_demand_cunning",        "You are outmatched today. Give up -- if not for your own sake, then think of your men!"),
  ("surrender_demand_sadistic",       "Surrender or I'll gut you like a tauntaun!"),
  ("surrender_demand_goodnatured",    "We have the advantage of you. Yield, and you will be well-treated."),
  ("surrender_demand_upstanding",     "You may fight us, but many of your men will be killed, and you will probably lose. Yield, and spare us both the unnecessary bloodshed."),

  ("surrender_offer_default",        "Stop! I yield!"),
  ("surrender_offer_martial",        "Stop! I yield!"),
  ("surrender_offer_quarrelsome",    "Enough! You win today, you dog! Ach, the shame of it!"),
  ("surrender_offer_pitiless",       "I yield! You have won. Cursed be this day!"),
  ("surrender_offer_cunning",        "Stop! I yield to you!"),
  ("surrender_offer_sadistic",       "I give up! I give up! Call back your dogs!"),
  ("surrender_offer_goodnatured",    "I yield! Congratulations on your victory, {sir/madame}!"),
  ("surrender_offer_upstanding",     "I yield! Grant me the honours of war, and do yourself credit!"),

  ("prisoner_released_default",       "You have my gratitude, {sir/madame}. I shall not forget your kindness."),
  ("prisoner_released_martial",       "You are indeed a {man/woman} of honour, {sir/madame}. I shall not forget this!"),
  ("prisoner_released_quarrelsome",   "I'm free? Well... Good bye, then."),
  ("prisoner_released_pitiless",      "Thank you. When you are finally defeated, I will request for your death to be swift and merciful. Unless, that is, you care to join us... Good bye, for now."),
  ("prisoner_released_cunning",       "Am I? You are a good {man/woman}. I will try to find a way to repay you."),
  ("prisoner_released_sadistic",      "Am I? So refined is your cruelty, that you would rather see me free and humiliated, than in chains. Enjoy your triumph!"),
  ("prisoner_released_goodnatured",   "You are indeed a {man/woman} of honour, {sir/madame}. I shall not forget this!"),
  ("prisoner_released_upstanding",    "You are indeed a {man/woman} of honour, {sir/madame}. I shall not forget this!"),

#Post 0907 changes begin
  ("enemy_meet_default",              "Who are you, that comes in arms against me?"),
  ("enemy_meet_martial",              "What is your name, {sir/madame}? If we come to blows, I would know whom I fight."),
  ("enemy_meet_quarrelsome",          "Who the hell are you?"),
  ("enemy_meet_pitiless",             "Who are you? Speak, so that I may know whom I slay."),
  ("enemy_meet_cunning",              "Tell me your name. It is always good to know your enemy."),
  ("enemy_meet_sadistic",             "Who are you? Speak quick, before I cut your tongue out."),
  ("enemy_meet_goodnatured",          "What is your name, {sir/madame}? If we come to blows, I would know whom I fight."),
  ("enemy_meet_upstanding",           "Who are you, who would come in arms to dispute our righteous cause?"),

  ("battle_won_default",              "You have proven yourself a most valued ally, today."),
  ("battle_won_martial",              "There is no greater fortune than the chance to show one's valor on the field of arms!"),
  ("battle_won_quarrelsome",          "Hah! We showed those bastards a thing or two, there, didn't we?"),
  ("battle_won_pitiless",             "Together, we will make the foe learn to fear our names, and to quail at our coming!"),
  ("battle_won_cunning",              "Now, we must be sure to press our advantage, so that the blood shed today is not wasted."),
  ("battle_won_sadistic",             "Now let us strip their dead and leave them for the crows, so that all will know the fate of those who come against us."),
  ("battle_won_goodnatured",          "That was a good scrap! No joy like the joy of victory, eh?"),
  ("battle_won_upstanding",           "Now, let us give thanks to the heavens for our victory, and mourn the many fine men who have fallen today."),

  ("battle_won_grudging_default",     "You helped turn the tide on the field, today. Whatever I may think of you, I cannot fault you for your valor."),
  ("battle_won_grudging_martial",     "{playername} -- you have shown yourself a worthy {man/woman} today, whatever your misdeeds in the past."),
  ("battle_won_grudging_quarrelsome", "Hmf. Yours is not a face which I normally like to see, but I suppose today I should thank you for your help."),
  ("battle_won_grudging_pitiless",    "Your help was most valuable today. I would not imagine that you came to help me out of kindness, but I nonetheless thank you."),
  ("battle_won_grudging_cunning",     "It would be unwise of me not to thank you for coming to help me in my hour of need. So... You have my gratitude."),
  ("battle_won_grudging_sadistic",    "Well! How touching! {playername} has come to rescue me."),
  ("battle_won_grudging_goodnatured", "{playername}! I can't say that we've always gotten along in the past, but you fought well today. My thanks to you!"),
  ("battle_won_grudging_upstanding",  "Perhaps I was wrong about you. Your arrival was most timely. You have my gratitude."),

  ("battle_won_unfriendly_default",         "So you're here. Well, better late than never, I suppose."),
  ("battle_won_unfriendly_martial",         "We have hard harsh words in the past, but for now let us simply enjoy our victory."),
  ("battle_won_unfriendly_quarrelsome",     "If you're standing there waiting for thanks, you can keep waiting. Your help wasn't really needed, but I guess you had nothing better to do, right?"),
  ("battle_won_unfriendly_pitiless",        "You have come here, like a jackal to a lion's kill. Very well then, help yourself to the spoils. I shall not stop you."),
  ("battle_won_unfriendly_cunning",         "{playername}... Well, I suppose your arrival didn't hurt, although I won't pretend that I'm happy to see you."),
  ("battle_won_unfriendly_sadistic",        "Back off, carrion fowl! This was my victory, however hard you try to steal the glory for yourself."),
  ("battle_won_unfriendly_goodnatured",     "Oh, it's you. Well, I suppose I should thank you for your help."),
  ("battle_won_unfriendly_upstanding",      "Thank you for coming to my support. Now I will be off, before I say something that I regret."),

  ("troop_train_request_default",               "I need someone like you to knock them into shape."),
  ("troop_train_request_martial",               "They need someone to show them the meaning of valor."),
  ("troop_train_request_quarrelsome",           "Fat lazy bastards. They make me puke."),
  ("troop_train_request_pitiless",              "They are more afraid of the enemy than they are of me, and this will not do."),
  ("troop_train_request_cunning",               "But men, like swords, are tempered and hardened by fire."),
  ("troop_train_request_sadistic",              "They need someone with steel in his back to flog some courage into them, or kill them trying."),
  ("troop_train_request_goodnatured",           "They're good enough lads, but I am afraid that they are not quite ready for a battle just yet."),
  ("troop_train_request_upstanding",            "It would be tantamount to murder for me to lead them into combat in their current state."),

  ("unprovoked_attack_default",               "What? Why do you attack us? Speak, you rascal!"),
  ("unprovoked_attack_martial",               "I have no objection to a trial of arms, but I would ask you for what reason you attack us?"),
  ("unprovoked_attack_quarrelsome",           "You're making a big mistake, {boy/girl}. What do you think you're doing?"),
  ("unprovoked_attack_pitiless",              "Indeed? If you really want to die today, I'd be more than happy to oblige you, but I am curious as to what you hope to accomplish."),
  ("unprovoked_attack_cunning",               "Really? I think that you are acting most unwisely. What do you hope to gain by this?"),
  ("unprovoked_attack_sadistic",              "What's this? Do you enjoy having your eyes put out?"),
  ("unprovoked_attack_goodnatured",           "Why do you do this? We've got no quarrel, {sir/madame}."),
  ("unprovoked_attack_upstanding",            "I consider this an unprovoked assault, and will protest to your king. Why do you do this?"),

  ("unnecessary_attack_default",               "I will not hesitate to cut you down if pressed, but I will offer you the chance to ride away from this."),
  ("unnecessary_attack_martial",               "I am eager to take you up on your challenge, {sir/madame}, although I will give you a minute to reconsider."),
  ("unnecessary_attack_quarrelsome",           "Bah! I'm in no mood for this nonsense today. Get out of my way."),
  ("unnecessary_attack_pitiless",              "I am in a merciful mood today. I will pretend that I did not hear you."),
  ("unnecessary_attack_cunning",               "I don't see what you have to gain by making an enemy of me. Maybe you should just ride away."),
  ("unnecessary_attack_sadistic",              "I have no time to waste on a worm like you. Get out of my way."),
  ("unnecessary_attack_goodnatured",           "I don't see what you have to gain by picking a fight, {sir/madame}. You can still ride away."),
  ("unnecessary_attack_upstanding",            "If a fight is what you wish, {sir/madame}, then you will have one, but I will yet offer you the chance to back down."),

  ("lord_challenged_default",                   "As you wish. Prepare to die!"),
  ("lord_challenged_martial",                   "So be it. Defend yourself!"),
  ("lord_challenged_quarrelsome",               "You impudent whelp! I'll crush you!"),
  ("lord_challenged_pitiless",                  "If you so badly wish to die, then I have no choice but to oblige you."),
  ("lord_challenged_cunning",                   "Well, if you leave me no choice..."),
  ("lord_challenged_sadistic",                  "You heap of filth! I'll make you wish you'd never been born."),
  ("lord_challenged_goodnatured",               "Very well. I had hoped that we might avoid coming to blows, but I see that have no choice."),
  ("lord_challenged_upstanding",                "So be it. It saddens me that you cannot be made to see reason."),

  ("lord_mission_failed_default",               "Well, I am disappointed, but I am sure that you will have many chances to redeem yourself."),
  ("lord_mission_failed_martial",               "There is no honour in failing a quest which you endeavoured to take, but I will accept your word on it."),
  ("lord_mission_failed_quarrelsome",           "You failed? Bah. I should have expected as much from the likes of you."),
  ("lord_mission_failed_pitiless",              "You failed? Well. You disappoint me. That is a most unwise thing to do."),
  ("lord_mission_failed_cunning",               "Well, I am disappointed, but no one can guarantee that the winds of fortune will always blow their way."),
  ("lord_mission_failed_sadistic",              "Indeed? Those who fail me do not always live to regret it."),
  ("lord_mission_failed_goodnatured",           "Oh well. It was a long shot, anyway. Thank you for making an effort."),
  ("lord_mission_failed_upstanding",            "Very well. I am sure that you gave it your best effort."),

  ("lord_follow_refusal_default",       "Follow you? You forget your station, {sir/madame}."),
  ("lord_follow_refusal_martial",       "Perhaps if you one day prove yourself a valorous and honourable warrior, then I would follow you. But not today."),
  ("lord_follow_refusal_quarrelsome",   "Follow someone like you? I don't think so."),
  ("lord_follow_refusal_pitiless",      "Leaders like me do not follow people like you, {sir/madame}."),
  ("lord_follow_refusal_cunning",       "First show me that you are the type of {man/woman} who will not lead me into disaster, and then perhaps I will follow you."),
  ("lord_follow_refusal_sadistic",      "I think not! Rather, you should follow me, as a whipped cur follows {his/her} master."),
  ("lord_follow_refusal_goodnatured",   "Um, I am a bit pressed with errands right now. Perhaps at a later date."),
  ("lord_follow_refusal_upstanding",    "First show me that you are worthy to lead, and then perhaps I will follow."),



  ("lord_insult_default",               "base varlot"),
  ("lord_insult_martial",               "dishonourable knave"),
  ("lord_insult_quarrelsome",           "filth-swilling bastard"),
  ("lord_insult_pitiless",              "low-born worm"),
  ("lord_insult_cunning",               "careless oaf"),
  ("lord_insult_sadistic",              "sniveling cur"),
  ("lord_insult_goodnatured",           "unpleasant fellow"),
  ("lord_insult_upstanding",            "disgraceful scoundrel"),


  ("rebellion_dilemma_default",                 "[liege]"),
  ("rebellion_dilemma_martial",                 "{s45} was clearly wronged. Although I gave an oath to {s46}, it does not bind me to support him if he usurped his throne illegally."),
  ("rebellion_dilemma_quarrelsome",             "Hmm. {s46} has never given me my due, so I don't figure I owe him much. However, maybe {s45} will be no better, and {s46} has at least shown himself ."),
  ("rebellion_dilemma_pitiless",                "Hmm. {s45} says {reg3?she:he} is the rightful heir to the throne. That is good -- it absolves me of my oath to {s46}. But still I must weight my decision carefully."),
  ("rebellion_dilemma_cunning",                 "Hmm. I gave an oath of homage to {s46}, yet the powerful are not bound by their oaths as our ordinary people. Our duty is to our own ability to rule, to impose order and prevent the war of all against all."),
  ("rebellion_dilemma_sadistic",                "Hmm. In this vile world, a wise man must think of himself, for no one else will. So -- what's in it for me?"),
  ("rebellion_dilemma_goodnatured",             "I do not know what to say. I gave an oath to {s46} as the lawful ruler, but if he is not the lawful ruler, I don't know if I am still bound."),
  ("rebellion_dilemma_upstanding",              "This is troublesome. It is a grave thing to declare my homage to {s46} to be null and void, and dissolve the bonds which keep our land from sinking into anarchy. Yet I am also pledged to support the legitimacy of the succession, and {s45} also has a valid claim to the throne."),

  ("rebellion_dilemma_2_default",               "[liege]"),
  ("rebellion_dilemma_2_martial",               "On the other hand, {s46} has led us in war and peace, and I am loathe to renounce my allegiance."),
  ("rebellion_dilemma_2_quarrelsome",           "So tell me, why should I turn my back on the bastard I know, in favor of {reg3?a woman:the bastard} I don't know?"),
  ("rebellion_dilemma_2_pitiless",              "It is a most perilous position to be in, to be asked whom I would make {reg3?ruler:king} of this land. Yet it is also a time of opportunity, for me to reap the rewards that have always been my due!"),
  ("rebellion_dilemma_2_cunning",               "{s46} has been challenged, and thus he will never be able to rule as strongly as one whose claim has never been questioned. Yet if {s45} takes the throne by force, {reg3?she:he} will not be as strong as one who succeeded peacefully."),
  ("rebellion_dilemma_2_sadistic",              "Perhaps if I join {s45} while {reg3?she:he} is still weak {reg3?she:he} will enrich me, but perhaps if I bring {s46} your head he will give me an even greater reward."),
  ("rebellion_dilemma_2_goodnatured",           "{s46} has always treated me decently, yet it's true that he did wrong to {s45}. I hesitate to renounce my homage to {s46}, yet I also don't think it's right to support injustice."),
  ("rebellion_dilemma_2_upstanding",            "I feel that I must do whatever is best for the realm, to avoid it being laid waste by civil war and ravaged by its enemies."),


  ("rebellion_prior_argument_very_favorable",   "I have already heard some arguments for supporting your candidate for the throne, and I tend to agree with them."),
  ("rebellion_prior_argument_favorable",        "I have already heard some arguments for supporting your candidate for the throne, and I tend to agree with them."),
  ("rebellion_prior_argument_unfavorable",      "I have already heard some arguments for supporting your candidate for the throne, but I do not find them convincing."),
  ("rebellion_prior_argument_very_unfavorable", "I have already heard some arguments for supporting your candidate for the throne, but I disagree with most of them."),

  ("rebellion_rival_default",                   "[liege]"),
  ("rebellion_rival_martial",                   "{s49} your ally {s44} once questioned my honour and my bravery. It's not often I get the chance to face him in battle, and make him retract his statement."),
  ("rebellion_rival_quarrelsome",               "{s49} you're working with {s44}. He's a crafty weasel, and I don't trust him one bit."),
  ("rebellion_rival_pitiless",                  "{s49} you seem to have enlisted the support of {s44} -- who is soft, and weak, and not fit to govern a fief, and whom I have always detested."),
  ("rebellion_rival_cunning",                   "{s49} {s44}, who has already joined you, is headstrong and quarrelsome, and a bit of liability."),
  ("rebellion_rival_sadistic",                  "{s49} I have no desire to fight alongside your ally {s44}, who puts on such a nauseating display of virtue."),
  ("rebellion_rival_goodnatured",               "{s49} I'd be reluctant to be on the same side as {s44}, who has quite a reputation for cruelty."),
  ("rebellion_rival_upstanding",                "{s49} your ally {s44} is in my opinion a dangerous, unreliable, and highly unprincipled man."),

  ("rebellion_argument_favorable",              "I respect your line of argument"),
  ("rebellion_argument_neutral",                "I find your line of argument only moderately compelling"),
  ("rebellion_argument_unfavorable",            "I do not find your line of argument compelling"),

  ("rebellion_persuasion_favorable",            "you state your case eloquently"),
  ("rebellion_persuasion_neutral",              "you make a reasonable case"),
  ("rebellion_persuasion_unfavorable",          "you make an unconvincing case"),

  ("rebellion_relation_very_favorable",         "I have the greatest respect for you personally."),
  ("rebellion_relation_favorable",              "I know and respect you personally."),
  ("rebellion_relation_neutral",                "I do not know you as well as I might like."),
  ("rebellion_relation_unfavorable",            "I do not trust you."),

  ("and_comma_3", "Furthermore, "),
  ("but_comma_3", "However,"),

  ("and_comma_1", ", and "),
  ("but_comma_1", ", but "),

  ("and_comma_2", ". Moreover, "),
  ("but_comma_2", ". Nonetheless, "),


  ("rebellion_agree_default",               "[liege]"),
  ("rebellion_agree_martial",               "I have decided. I will back {s45} as the rightful heir."),
  ("rebellion_agree_quarrelsome",           "Ahh, I've thought long enough. I never did like {s46} much anyway. Let's go take his throne away from him."),
  ("rebellion_agree_pitiless",              "You are fortunate. I have decided to join you. Pray do not give me cause to regret this decision."),
  ("rebellion_agree_cunning",               "This is a most dangerous decision, but after careful consideration, I have decided that I will join you. Let's hope it is for the best."),
  ("rebellion_agree_sadistic",              "I have decided. I will back your {reg3?woman:man} {s45}. But you'd best make sure that {reg3?she:he} rewards me well!"),
  ("rebellion_agree_goodnatured",           "All right. I think your {reg3?woman:man} will be a good ruler. I'll join you."),
  ("rebellion_agree_upstanding",            "So be it. My first duty is to this realm, and to save it from lawlessness I will back {s45} and renounce my homage to {s46}. May the Heavens forgive me if I do wrong."),


  ("rebellion_refuse_default",              "[liege]"),
  ("rebellion_refuse_martial",              "I am sorry. {s45} has a good claim, but it's not enough for me to turn my back on {s46}. I will remain loyal to my liege."),
  ("rebellion_refuse_quarrelsome",          "Nah. Your whelp {s45} doesn't have what it takes to rule this realm. I'm sticking with {s46}."),
  ("rebellion_agree_pitiless",              "No. I will not join your rebellion. I count it little more than the tantrum of a child, denied a bauble which {reg3?she:he} thinks should be {reg3?hers:his}. I will stick with {s46}, whose ability to rule is well-tested."),
  ("rebellion_agree_cunning",               "I am sorry. You do not give me reason for confidence that you will win. Many will die, but I do not wish to be among them. I will continue to back {s46}."),
  ("rebellion_agree_sadistic",              "No. I won't play your little game. You grasp at a crown, but I think instead you'll get a quick trip to the scaffold, and I'll be there by {s46}'s side to watch the headsman's axe drop."),
  ("rebellion_agree_goodnatured",           "I am sorry. I don't feel right turning my back on {s46}. No hard feelings when me meet on the battlefield."),
  ("rebellion_agree_upstanding",            "I am sorry. {s45}'s claim is not strong enough for me to inflict the curse of civil disorder on the poor wretches of this land. I will continue to back {s46}. May the Heavens forgive me if I do wrong."),

  ("talk_later_default",                    "[liege]"),
  ("talk_later_martial",                    "Now is not the time to talk politics! I am here today with my fellow leaders, armed for battle. You'd better prepare to fight."),
  ("talk_later_quarrelsome",                "Do you expect me to discuss betraying my liege with you, while we are surrounded by his army? What do you take me for, a bloody idiot?"),
  ("talk_later_pitiless",                   "Still your tongue! Whatever I have to say on this matter, I will not say it here and now, while we are in the midst of our army."),
  ("talk_later_cunning",                    "This is hardly the time or the place for such a discussion. Perhaps we can discuss it at a later time and a different place, but for now we're still foes."),
  ("talk_later_sadistic",                   "You should have your mouth sewn shut! Can you imagine what would happen if the other commanders see me talking to you of treason?"),
  ("talk_later_goodnatured",                "So you wish to discuss your rebellion with me? Try that again when we aren't surrounded by my liege's army, and I will hear what you have to say."),
  ("talk_later_upstanding",                 "Whatever my thoughts on the legitimacy of the succession, I am not about to discuss them here and now. If we meet again when we can talk in privacy, I will hear what you have to say on the matter. But for now, consider me your enemy."),


  ("gossip_about_character_default",        "They say that {s6} doesn't possess any interesting character traits."),
  ("gossip_about_character_martial",        "They say that {s6} loves nothing more than war."),
  ("gossip_about_character_quarrelsome",    "They say that {s6} almost came to blows with another commander lately, because the man made a joke about his nose."),
  ("gossip_about_character_selfrighteous",  "I heard that {s6} had a squire executed because the unfortunate man killed a deer in his forest."),
  ("gossip_about_character_cunning",        "They say that {s6} is a cunning opponent."),
  ("gossip_about_character_sadistic",       "They say that {s6} likes to torture his enemies. I wouldn't want to get on the bad side of that man."),
  ("gossip_about_character_goodnatured",    "They say that {s6} is a good man and treats people living in his lands decently. That is more than what can be said for most of the nobles."),
  ("gossip_about_character_upstanding",     "People say that it is good to be in the service of {s6}. He is good to his followers, and rewards them if they work well."),

  ("latest_rumor",        "The latest rumor you heard about {s6} was:"),


#steve post 0912 changes begin

  ("swadian_rebellion_pretender_intro",    "I am Isolla, rightful Queen of the Swadians."),
  ("vaegir_rebellion_pretender_intro",     "My name is Valdym. Some men call me 'the Bastard.' I am a prince of the Vaegirs, but by all rights I should be their king, instead of my cousin Yaroglek."),
  ("khergit_rebellion_pretender_intro",    "I am Dustum Khan, son of Janakir Khan, and rightful Khan of the Khergits."),
  ("nord_rebellion_pretender_intro",       "I am Lethwin Far-Seeker, son of Hakrim the Old, who should be king of the Nords of Calradia."),
  ("rhodok_rebellion_pretender_intro",     "I am Lord Kastor, the rightful King of the Rhodoks, who will free them from tyranny."),

  ("swadian_rebellion_pretender_story_1",  "I was the only child of my father, King Esterich. Although I am a woman, he loved me like a son and named me his heir -- not once, but several times, before the grandest nobles of the land so that none could doubt his intention. There is no law that bars a woman from ruling -- indeed, we Swadians tell tales of warrior queens who ruled us in our distant past."),
  ("vaegir_rebellion_pretender_story_1",   "My father died when I was young, leaving me in the care of his brother, the regent Burelek. But rather than hold the throne until I came of age, this usurper used his newfound power to accuse my mother of adultery, and to claim that I was not my father's son. She was executed for treason, and I was declared a bastard."),
  ("khergit_rebellion_pretender_story_1",  "Sanjar Khan and I are brothers, sons of the old Janakir Khan, although of different mothers. Although I was the younger brother, all those who knew the old Khan will testify that throughout my father's life, I was his favorite, entrusted with the responsibilities of government. Sanjar busied himself with hunts and feasts to win the affection of the more dissolate of my father's commanders."),
  ("nord_rebellion_pretender_story_1",     "I am called the Far-Seeker because I have travelled great distances, even by the standards of the Nords, in search of knowledge. Before I came of age, my father sent me abroad on a tour of study at the courts and universities in the lands overseas. If the Nords are to call themselves the heirs of the Calradian empire, then they must act the part, and know something of law and letters, and not call themselves content merely to fight, plunder, and drink."),
  ("rhodok_rebellion_pretender_story_1",   "The Rhodoks are a free people, and not slaves to any hereditary monarch. The king must be chosen from one of the leading noble families of the land, by a council drawn by lot from the patricians of the cities of Jelkala, Veluca, and Yalen. The council meets on a field before Jelkala, and no man is allowed to appear in arms during their deliberations, on pain of death."),

  ("swadian_rebellion_pretender_story_2",  "Yet when my father died, his cousin Harlaus convinced the nobles that no Swadian king of sound mind could name a woman as his heir. Harlaus said that his designation of me was the act of a madman, and thus had no legal standing, and that he, as my father's closest male relative, should of take the throne."),
  ("vaegir_rebellion_pretender_story_2",   "I was smuggled abroad by a faithful servant, but now I am of age and have returned to reclaim what is rightfully mine. Burelek died soon after his act of perfidy -- the judgment of heaven, no doubt. His son Yaroglek now calls himself king, but as his claim is tainted, he is no less a usurper than his father, and I will topple him from his throne."),
  ("khergit_rebellion_pretender_story_2",  "According to Khergit custom, when a man dies his herds are split between all his sons, equally. So too it is with the khanate. When I heard of my father's death, I was away inspecting our borders, but I hurried home to Tulga, ready to give Sanjar his due and share the khanate with him. But when I arrived, I found that he rushed his supporters to the court, to have himself proclaimed as the sole khan."),
  ("nord_rebellion_pretender_story_2",     "My father died however before I completed my course of study, and as I hurried home to claim his throne my ship was wrecked by a storm. One of my father's thanes, Ragnar, seized this opportunity and spread rumors that I had died abroad. He summoned a gathering of his supporters to have himself proclaimed king, and has taken the past few years to consolidate his power."),
  ("rhodok_rebellion_pretender_story_2",   "During the last selection, there were but two candidates, myself, and Lord Graveth. While the council was deliberating, Graveth appeared, sword in hand, telling them that a Swadian raiding party was about to descend on the field of deliberation -- which was true, by the way -- and if he were not elected king, then he would leave them to their fate."),

  ("swadian_rebellion_pretender_story_3",  "I will admit that I did my cause no good by cursing Harlaus and all who listened to him as traitors, but I also believe that the magistrates who ruled in his favor were bought. No matter -- I will raise an army of loyal subjects, who would honour their old king's memory and will. And if anyone doubts that a woman can wield power, then I will prove them wrong by taking Harlaus' ill-gotten crown away from him."),
  ("vaegir_rebellion_pretender_story_3",   "Until I have my rights restored in the sight of all the Vaegirs, I will bear the sobriquet, 'the Bastard', to remind me of what I must do."),
  ("khergit_rebellion_pretender_story_3",  "My brother thinks that Khergits will only respect strength: a leader who takes what he wants, when he wants it. But I think that he misreads the spirit of our people.--we admire a resolute leader, but even more we a just one, and we know that a man who does not respect his own brother's rights will not respect the rights of his followers."),
  ("nord_rebellion_pretender_story_3",     "So I remain in exile -- except now I am not looking for sages to tutor me in the wisdom of faraway lands, but warriors, to come with me back to the land of the Nords and regain my throne. If Ragnar doubts my ability to rule, then let him say so face to face, as we stare at each other over the rims of our shields. For a warrior can be a scholar, and a scholar a warrior, and to my mind, only one who combines the two is fit to be king!"),
  ("rhodok_rebellion_pretender_story_3",   "Well, Graveth defeated the Swadians, and for that, as a Rhodok, I am grateful. When I am king, I will myself place the wreath of victory on his head. But after that I will have it separated from his shoulders, for by his actions he has shown himself a traitor to the Rhodok confederacy and its sacred custom."),

  ("swadian_rebellion_monarch_response_1", "Isolla thinks she should be Queen of the Swadians? Well, King Esterich had a kind heart, and doted on his daughter, but a good-hearted king who doesn't use his head can be a curse to his people. Isolla may tell you stories of warrior queens of old, but you might also recall that all the old legends end in the same way -- with the Swadians crushed underfoot by the armies of the Calradic Emperor."),
  ("vaegir_rebellion_monarch_response_1",  "Were Valdym to come to me in peace, I would laden him with titles and honours, and he would become the greatest of my commanders. But as he comes in war, I will drag him before me in chains and make him acknowledge me as rightful sovereign, then cut his tongue from his mouth so that he cannot recant."),
  ("khergit_rebellion_monarch_response_1", "My brother Dustum has perhaps told you of his insistence upon splitting the khanate, as though it were a herd of sheep. Let me tell you something. Ever since the Khergits established themselves on this land, the death of every khan has had the same result -- the land was divided, the khan's sons went to war, and the strongest took it all anyway. I simply had the foresight to stave off the civil war in advance."),
  ("nord_rebellion_monarch_response_1",    "Lethwin 'Far-Seeker'? Lethwin Inkfingers, is more like it. Perhaps you have heard the expression, 'Unhappy is the land whose king is a child.' Unhappy too is the land whose king is a student. You want the Nords to be ruled by a beardless youth, whose hand bears no callouses left by a sword's grip, who has never stood in a shield wall? If Lethwin were king, his thanes would laugh at him to his face!"),
  ("rhodok_rebellion_monarch_response_1",  "No doubt Lord Kastor told you that I defiled the hallowed Rhodok custom by interfering with the patricians' election of a king. Well, let me tell you something. The patricians of the planet make longwinded speeches about our ancient liberties, but then choose as their king whichever noble last sat in their villa and sipped a fine wine and promised to overlook their unpaid taxes."),

  ("swadian_rebellion_monarch_response_2", "Those who weep for the plight of a Swadian princess denied her father's throne should reflect instead on the fate of a Swadian herdswoman seized by a Vaegir raider and taken as chattel to the slave markets. Talk to me of queens and old stories when our warlike neighbors are vanquished, and our land is at peace."),
  ("vaegir_rebellion_monarch_response_2",  "Whatever my father may or may not have done to secure the throne does not matter. I have inherited it, and that is final. If every old claim were to be brought up anew, if every man's inheritance could be called into question at any time, then it would be the end of the institution of kingship, and we would live in a state of constant civil war."),
  ("khergit_rebellion_monarch_response_2", "Dustum would make a fine assessor of flocks, or adjudicator of land disputes. But can you imagine such a man as khan? We would be run off of our land in no time by our neighbors, and return to our old days of starving and freezing on the steppe."),
  ("nord_rebellion_monarch_response_2",    "Old Hakrim may have had fancy ideas about how to dispose of his faction, but it is not just royal blood that makes a King of the Nords. I am king by acclamation of the thanes, and by right of being the strongest. That counts for more than blood, and woe to any man in this land who says otherwise."),
  ("rhodok_rebellion_monarch_response_2",  "The only liberty that concerns them is their liberty to grow fat. Meanwhile, my men sleep out on the steppe, and eat dry bread and salt fish, and scan the horizon for burning villages, and shed our blood to keep the caravan routes open. Here's an idea -- if I ever meet a merchant who limps from a Khergit arrow-wound or a Swadian sword-stroke, then I'll say, 'Here's a man whose counsel is worth taking.'"),


#steve post 0912 changes end




  ("credits_1", "Mount&Blade Copyright 2001-2008 Taleworlds Entertainment"),
  ("credits_2", "Game design:^Armagan Yavuz^Steve Negus^Cem Cimenbicer"),
  ("credits_3", "Programming:^Armagan Yavuz^Cem Cimenbicer"),
  ("credits_4", "CG Artists:^Ipek Yavuz^Ozgur Saral^Mustafa Ozturk"),
  ("credits_8", "Animation:^Pinar Cekic^Umit Singil"),  
  ("credits_5", "Concept Artist:^Ganbat Badamkhand"),
  ("credits_6", "Writing:^Steve Negus^Ryan A. Span^Armagan Yavuz"),
  ("credits_9", "Original Music:^Jesse Hopkins"),
  ("credits_7", "Additional Modeling:^Hilmi Aric^Ahmet Sarisakal^Katie Beedham^^^Additional Writing:^Michael Buhler^Patrick Desjardins^^^Voice Talents:^Tassilo Egloffstein^Jade E Henderson^^^\
Original Music Composed by:^Jesse Hopkins^\
Violin Solos Performed by:^Zoriy Zinger^\
Main Theme and Scherzo Performed by:^The Russian State Symphony Cinema Orchestra, Conducted by Sergei Skripka^^^\
Sound Samples:^Audiosparx.com^^^\
Mount&Blade Map Editor:^Matt Stentiford^^^\
Taleworlds Forum Programming:^Brett Flannigan www.fenrisoft.com^^^\
Mount&Blade Tutorial written by:^Edward Spoerl^^^\
Gameplay Videos:^Jemes Muia^^^\
Motion Capture System:^NaturalPoint-Optitrack Arena^^^\
Horse Motion Capture Animation Supplied by:^Richard Widgery & Kinetic Impulse^^^\
Ragdoll Physics:^Newton Game Dynamics^^^\
Sound and Music Program Library:^FMOD Sound System by Firelight Technologies^^^\
Copy Protection:^Themida by Oreans Technologies^^^\
Skybox Textures:^Jay Weston www.hyperfocaldesign.com^^^\
Third Party Art Libraries Used:^Texturemonk^Mayang Textures^cgtextures.com^3d.sk^^\
Unofficial Mount&Blade Editor:^Josh Dahlby^^^\
Many thanks to Marco Tarini for the Mountain shader idea!^^^\
Special Thanks to:^Ibrahim Dogan^Nova Language Works^Selim Kurtulus and UPS Turkey^^^\
Taleworlds.com Forum Administrators and Moderators:^Janus^Archonsod^Narcissus^Nairagorn^Lost Lamb^Deus Ex^Merentha^Volkier^Okin^Instag0\
^Deniz^ego^Guspav^Hallequin^Invictus^okiN^Raz^rejenorst^Skyrage^ThVaz^^^\
Spanish Translation^^Translators:^Anabel 'Rhaenys' Diaz^Analia 'Immortality' Dobarro^Anoik^^Medieval Consultant:^Enric 'Palafoxx' Clave^^Language Tester:^Theo de Moree^^^\
Mount&Blade Community Suggestions and Feedback:^\
13 Chain Bloody Spider^\
Aenarion^\
AgentSword^\
Ahadhran^\
Albino^\
Allegro^\
allthesedamnnamesare^\
Amman de Stazia^\
Ancientwanker^\
Anrea 'Skree' Giongiani^\
Aqtai^\
Art Falmingaid^\
bryce777^\
Bugman^\
Buxton^\
Calandale^\
Cartread^\
Chel^\
Chilly5^\
Cirdan^\
Cleaning agent^\
Cymro^\
DaBlade^\
DaLagga^\
Damien^\
danover^\
Dearahn^\
Deathblow^\
Destichado^\
Dryvus^\
dunnno^\
D'Sparil^\
ealabor^\
Ealdormann Hussey^\
EasyCo506^\
El Duke^\
Elias Maluco^\
Eogan^\
ex_ottoyuhr^\
Fisheye^\
Fossi^\
fujiwara^\
Fuzzpilz^\
GandalfTheGrey^\
Gerif^\
Grocat^\
Guspav^\
Halden The Borch shooter^\
Hallequin^\
Handel^\
Hardcode^\
Haupper^\
Hellequin^\
Highelf^\
Highlander^\
Ibrahim Turgut^\
Iesu^\
Ilex^\
Ingolifs^\
Invictus^\
Itchrelief^\
Jlgx50^\
JHermes^\
Jik^\
john259^\
JonathanStrange^\
jpgray^\
kamov23^\
Kayback^\
Khalid Ibn Walid^\
KON_Air^\
Lady Tanith^\
Larry Knight^\
LavaLampMaster^\
Leprechaun^\
Lhorkan^\
Llew2^\
Maelstorm^\
Manitas^\
Maw^\
MAXHARDMAN^\
Merentha^\
Merlkir^\
Michael Elijah 'ironpants' Bell-Rao^\
mihoshi^\
Mirathei^\
mkeller^\
Momaw^\
Morgoth2005^\
MrCrotch^\
mtarini^\
n00854180t^\
Naridill^\
Nicholas Altaman\
okiN^\
oksir^\
Oldtimer^\
Ollieh^\
oRGy^\
Oubliette^\
Patrick 'nox' Gallaty^\
Pavlov^\
Rando^\
Raz^\
rejenorst^\
Rjii^\
Ron Losey^\
Rorthic^\
RR_raptor^\
Scion^\
Seff^\
shenzay^\
Shadowmoses^\
shikamaru 1993^\
Silver^\
silverkatana^\
Sir Prince^\
Sirgigor^\
Skyrage^\
Smoson^\
sneakey pete^\
Stefano^\
Stella^\
Stonewall382^\
Talak^\
Tankai^\
TG^\
thelast^\
The Phoenix^\
The Pope^\
The Yogi^\
Thingy Master^\
Thormac^\
Thus_Spake_Nosferatu^\
ThVaz^\
Toygar Birinci^\
Tuckles^\
Tul^\
Ursca^\
Vaerraent^\
Vilhjalmr^\
Volkier^\
vuk^\
Wanderer^\
WhoCares^\
Winter^\
Worbah^\
Yoshiboy^\
...and many many other wonderful Mount&Blade players!^^\
(This is only a small sample of all the players who have contributed to the game by providing suggestions and feedback.^\
This list has been compiled by sampling only a few threads in the Taleworlds Forums.^\
Unfortunately compiling an exhaustive list is almost impossible.^\
We apologize sincerely if you contributed your suggestions and feedback but were not listed here, and please know that we are grateful to you all the same...)\
"),
  ("credits_10", "Paradox Interactive^^President and CEO:^Theodore Bergqvist^^Executive Vice President:^Fredrik Wester\
^^Chief Financial Officer:^Lena Eriksson^^Finance & Accounting:^Annlouise Larsson^^VP Sales & Marketing US:^Reena M. Miranda\
^^VP Sales & Marketing EU:^Martin Sirc^^Distribution Manager Nordic:^Erik Helmfridsson^^Director of PR & Marketing:^Susana Meza\
^^PR & Marketing:^Sofia Forsgren^^Product Manager:^Boel Bermann\
"),
  ("credits_11", "Logotype:^Jason Brown^^Cover Art:^Piotr Fox Wysocki\
^^Layout:^Christian Sabe^Melina Grundel^^Poster:^Piotr Fox Wysocki^^Map & Concept Art:^Ganbat Badamkhand\
^^Manual Editing:^Digital Wordsmithing: Ryan Newman, Nick Stewart^^Web:^Martin Ericsson^^Marketing Assets:^2Coats\
^^Localization:^S&H Entertainment Localization^^GamersGate:^Ulf Hedblom^Andreas Pousette^Martin Ericson^Christoffer Lindberg\
"),
  ("credits_12", "Thanks to all of our partners worldwide, in particular long-term partners:\
^Koch Media (Germany & UK)^Blue Label (Italy & France)^Friendware (Spain)^New Era Interactive Media Co. Ltd. (Asia)\
^Snowball (Russia)^Pinnacle (UK)^Porto Editora (Portugal)^Hell-Tech (Greece)^CD Projekt (Poland, Czech Republic, Slovakia & Hungary)\
^Paradox Scandinavian Distribution (Scandinavia)\
"),  

# START OF CUSTOM BATTLE MOD
##########################################
# Custom Battle Strings
##########################################

# No choice made
  ("no_choice", "None"),
  
# Faction Choice Strings
#  ("galacticempire", "Faction of Vaegirs"),
  ("galacticempire", "Galactic Empire"),  
#  ("rebelalliance", "Faction of Swadia"),
  ("rebelalliance", "Rebel Alliance"),  
#  ("huttcartel", "Faction of Nords"),
  ("huttcartel", "Hutt Cartel"),
#  ("faction_4", "Kindgom of Rhodok"),
  ("faction_4", "Mercenaries"),
  ("faction_5", "Clone Wars"),
  ("no_faction", "N/A"),
  
# Map Choice Strings
  ("custom_battle_location_1", "Geonosis - V. Large"),
  #("custom_battle_location_2", "Deep Forest - Large"),
  ("custom_battle_location_2", "Yavin IV Plains - Large"),
  ("custom_battle_location_3", "Dagobah Swamp - Medium"),
  
# Map Type Strings
  ("custom_battle_type_1", "One Vs One"),
  ("custom_battle_type_2", "Three Way"),
  ("custom_battle_type_3", "Four Way"),
  ("custom_battle_type_4", "Five Way"),
  ("custom_battle_type_5", "Six Way"),
  ("custom_battle_type_6", "Two Vs Two"),
  
  ("custom_battle_rain_0", "None"),
  ("custom_battle_rain_1", "Rain - Light"),
  ("custom_battle_rain_2", "Rain - Medium"),
  ("custom_battle_rain_3", "Rain - Heavy"),
  ("custom_battle_rain_4", "Snow - Light"),
  ("custom_battle_rain_5", "Snow - Medium"),
  ("custom_battle_rain_6", "Snow - Heavy"),
  
  ("custom_battle_fog_0", "None"),
  ("custom_battle_fog_1", "Light"),
  ("custom_battle_fog_2", "Medium"),
  ("custom_battle_fog_3", "Heavy"),

  ("custom_battle_time_0", "Midday"),
  ("custom_battle_time_1", "Sunset"),
  ("custom_battle_time_2", "Night"),
  ("custom_battle_time_3", "Dawn"),
 
 # END OF CUSTOM BATTLE MOD

#SW BSG integration
  ("space_combat_practice", "Please board the spaceship to begin^^CONTROLS:^w / s = increase / decrease speed^a / d = rotate left / right^left mouse / space = fire lasers^mouse = change direction while moving^t key = toggle vertical control^^NOTE:  This is a training mission, please press the TAB key to exit when you are done."),

# ("viper_status", "Speed: {reg1}'cms. Damage: {reg2}. Missiles: {reg3}. Cannons: {reg4}. cylon1: {reg5}. cylon2: {reg6}. cylon3: {reg7}. cylon4: {reg8}.\
# cylon5: {reg9}. cylon6: {reg10}. cylon7: {reg11}. cylon8: {reg12}. viper1: {reg13}. viper2: {reg14}. viper3: {reg15}. viper4: {reg16}.\
# viper5: {reg17}. viper6: {reg18}. viper7: {reg9}. viper8: {reg20}."),
("viper_status", "PLAYER: Speed: {reg1}'cms. Damage: {reg2}. Missiles: {reg3}. Cannons: {reg4}.^             gold1: {reg13}. gold2: {reg14}. gold3: {reg15}. gold4: {reg16}. gold5: {reg17}. gold6: {reg18}. gold7: {reg9}. gold8: {reg20}.^ENEMY: blue1: {reg5}. blue2: {reg6}. blue3: {reg7}. blue4: {reg8}. blue5: {reg9}. blue6: {reg10}. blue7: {reg11}. blue8: {reg12}."),
 # with debug line below
 #("viper_status", "PLAYER: Speed: {reg1}'cms. Damage: {reg2}. Missiles: {reg3}. Cannons: {reg4}.^             gold1: {reg13}. gold2: {reg14}. gold3: {reg15}. gold4: {reg16}. gold5: {reg17}. gold6: {reg18}. gold7: {reg9}. gold8: {reg20}.^ENEMY: blue1: {reg5}. blue2: {reg6}. blue3: {reg7}. blue4: {reg8}. blue5: {reg9}. blue6: {reg10}. blue7: {reg11}. blue8: {reg12}.^^^@DEBUG: x = {reg21}, y = {reg22}"),

###################################################################################
# Autoloot
###################################################################################
	("none", "none"),

	("item_pool_no_items", "There are currently no items in the item pool."),
	("item_pool_one_item", "There is one item left in the item pool."),
	("item_pool_many_items", "There are {reg20} items left in the item pool."),
	("item_pool_abandon", "Abandon the items in the item pool and continue."),
	("item_pool_leave", "Done."),
	
	("hero_not_upgrading_armor","not upgrading my armor"),
	("hero_upgrading_armor","upgrading my own armor"),
	("hero_not_upgrading_horse","not upgrading my transportation"),
	("hero_upgrading_horse","upgrading my own transportation"),

	# HC - make sure the commented number corresponds to the position/number of the item types in header_items.py.
	#	   DO NOT remove any strings that aren't used, else they won't "line up" with the declarations in header_items.py.
	("hero_wpn_slot_none","Keep current ({s10})"), #0
	("hero_wpn_slot_horse","Horse"), #1 to maintain compatibility with header_items (item type 1 is horse)
	("hero_wpn_slot_one_handed","One-handed Weapon"), #2
	("hero_wpn_slot_two_handed","Two-handed Weapon"),  #3
	("hero_wpn_slot_polearm_all","Polearm"), #4
	("hero_wpn_slot_arrows","Arrows (should not see)"), #5
	("hero_wpn_slot_bolts","Bolts (should not see)"), #6
	("hero_wpn_slot_shield","Shield"), #7
	("hero_wpn_slot_pistols","Bow (should not see)"), #8
	("hero_wpn_slot_musket","Crossbow (should not see)"), #9
	("hero_wpn_slot_throwing","Throwing Weapon"), #10
	("hero_wpn_slot_goods","Do not use. Placeholder only."), #11
	("hero_wpn_slot_head_armor","Do not use. Placeholder only."), #12
	("hero_wpn_slot_body_armor","Do not use. Placeholder only."), #13
	("hero_wpn_slot_foot_armor","Do not use. Placeholder only."), #14
	("hero_wpn_slot_hand_armor","Do not use. Placeholder only."), #15
	("hero_wpn_slot_pistol","Laser Pistols"), #16
	("hero_wpn_slot_musket","Laser Rifles"), #17
	("hero_wpn_slot_ammo","Plasma Gas Cartidges"), #18
	
###################################################################################
# End Autoloot
###################################################################################

	("cantina_rand_msg_1","I'm trying to drink, stop bothering me and go crink yourself."),
	("cantina_rand_msg_2","What the brix are you doing, leave me alone."),
	("cantina_rand_msg_3","You smell like bantha breath, get out of my face."),
	("cantina_rand_msg_4","Don't bother me or I will grease you."),
	("cantina_rand_msg_5","You look like a nerfherder, I don't bother with people like you."),
	("cantina_rand_msg_6","I've lost my job and am blaster-happy right now, it is best not to bother me."),
	("cantina_rand_msg_7","I have the death sentence in twelve systems, you better be careful or you'll be dead."),
	("cantina_rand_msg_8","Droyk! Who do you think you are, leave me alone."),
	("cantina_rand_msg_9","You look new here, so some advice about these Cantina's. You will never find a more wretched hive of scum and villainy, you must be cautious."),
	("cantina_rand_msg_10","My jawa juice was just freshly-squeezed, please let me finish it in peace."),

	("cantina_joke_1","Q:  What do you call a Sith who won't fight?^^A:  A Sithy."),
	("cantina_joke_2","Q:  How is Ducktape like the Force?^^A:  It has a dark side, a light side and it binds the galaxy together."),
	("cantina_joke_3","Q:  How many stormtroopers does it take to replace a lightbulb?^^A:  Two, one to screw the bulb in, the other to shoot him and take the credit."),
	("cantina_joke_4","Q:  What goes, 'Ha, ha, ha, haaaa.... AGGGHHHH! Thump'?^^A:  An Imperial Officer laughing at Darth Vader."),
	("cantina_joke_5","Q:  Why did Yoda cross the road?^^A:  Because the chickens Forced him to."),
	("cantina_joke_6","Q:  Why did the Ewok fall out of the tree?^^A:  It was dead."),
	("cantina_joke_7","Q:  What do you call a person who brings a rancor its dinner?^^A:  The appetizer."),
	("cantina_joke_8","Q:  Why do Doctors make the best Jedi?^^A:  Because a Jedi must have patience."),
	("cantina_joke_9","Q:  What's the name of the worst cantina on Coruscant?^^A:  The Ackbar."),
	("cantina_joke_10","Q:  What did the rancor say after he ate a Wookiee?^^A:  Chewie!"),	

#own faction start-----------------------------------
#SW - modified all center_1_faction and higher names
#towns
  ("center_1_faction", "Player Faction"),
  ("center_2_faction", "Player Faction"),
  ("center_3_faction", "Player Faction"),
  ("center_4_faction", "Player Faction"),
  ("center_5_faction", "Player Faction"),
  ("center_6_faction", "Player Faction"),
  ("center_7_faction", "Player Faction"),
  ("center_8_faction", "Player Faction"),
  ("center_9_faction", "Player Faction"),
  ("center_10_faction", "Player Faction"),
  ("center_11_faction", "Player Faction"),
  ("center_12_faction", "Player Faction"),
  ("center_13_faction", "Player Faction"),
  ("center_14_faction", "Player Faction"),
  ("center_15_faction", "Player Faction"),
  ("center_16_faction", "Player Faction"),
  ("center_17_faction", "Player Faction"),
  ("center_18_faction", "Player Faction"),
#castles  
  ("center_19_faction", "Player Faction"),
  ("center_20_faction", "Player Faction"),
  ("center_21_faction", "Player Faction"),
  ("center_22_faction", "Player Faction"),
  ("center_23_faction", "Player Faction"),
  ("center_24_faction", "Player Faction"),
  ("center_25_faction", "Player Faction"),
  ("center_26_faction", "Player Faction"),
  ("center_27_faction", "Player Faction"),
  ("center_28_faction", "Player Faction"),
  ("center_29_faction", "Player Faction"),
  ("center_30_faction", "Player Faction"),
  ("center_31_faction", "Player Faction"),
  ("center_32_faction", "Player Faction"),
  ("center_33_faction", "Player Faction"),
  ("center_34_faction", "Player Faction"),
  ("center_35_faction", "Player Faction"),
  ("center_36_faction", "Player Faction"),
  ("center_37_faction", "Player Faction"),
  ("center_38_faction", "Player Faction"),
  ("center_39_faction", "Player Faction"),
  ("center_40_faction", "Player Faction"),
  ("center_41_faction", "Player Faction"),
  ("center_42_faction", "Player Faction"),
  ("center_43_faction", "Player Faction"),
  ("center_44_faction", "Player Faction"),
  ("center_45_faction", "Player Faction"),
  ("center_46_faction", "Player Faction"),
  ("center_47_faction", "Player Faction"),
  ("center_48_faction", "Player Faction"),
  ("center_49_faction", "Player Faction"),
  ("center_50_faction", "Player Faction"),  
  ("center_51_faction", "Player Faction"),    
  ("center_52_faction", "Player Faction"),    
  ("center_53_faction", "Player Faction"),    
  ("center_54_faction", "Player Faction"),    
  ("center_55_faction", "Player Faction"),    
  ("center_56_faction", "Player Faction"),    
  ("center_57_faction", "Player Faction"),    
  ("center_58_faction", "Player Faction"),
#own faction end-----------------------------------	

#SW - spaceship strings start
  #empire
  ("spaceship_imperial_star_destroyer_name", "Imperial Star Destroyer"),
  #("spaceship_imperial_star_destroyer_desc", "Fire power, cargo space and scanners.^The Imperial Star Destroyer is more than versatile. ^^It comes standard with two troop compartments but these ^can be extended to a whopping six.^^Prisoners are also no problem, with between two and four bays available. ^^The ISD has a basic medical facility which can be improved to a MK-II model. ^^The scanners and drive are both MK-I models and can be upgraded to MK-III. ^^Finally, the ship can support a combat computer up to MK-IV, ^with a MK-II unit installed standard."),
  ("spaceship_imperial_star_destroyer_desc", "If you're after loads of space for your troops, ^the Imperial Star Destroyer is the way to go."),
  ("spaceship_imperial_star_destroyer_interdictor_name", "Imperial Interdictor Star Destroyer"),
  #("spaceship_imperial_star_destroyer_interdictor_desc", "If you're after loads of space for your troops, ^the Imperial Interdictor Star Destroyer is the way to go. ^^It comes standard with two troop compartments but these ^can be extended to a whopping six.^^Prisoners are also no problem, with between two and four bays available. ^^The ISD has a basic medical facility which can be improved to a MK-II model. ^^The scanners and drive are both MK-I models and can be upgraded to MK-IV. ^^Finally, the ship can support a combat computer up to MK-V, ^with a MK-II unit installed standard."),
  ("spaceship_imperial_star_destroyer_interdictor_desc", "The Interdictor Star Destroyer isn't designed for heavy line combat, ^but it's excellent for tracking medium size ships."),
  ("spaceship_imperial_dreadnaught_frigate_name", "Imperial Dreadnaught Heavy Cruiser"),
  ("spaceship_imperial_dreadnaught_frigate_desc", "The Imperial Dreadnought might be outdated, but it fields a great ^fire power and is still respected by both rebels and imperials."),
  ("spaceship_imperial_victory_c2_frigate_name", "Imperial Victory-II Frigate"),
  ("spaceship_imperial_victory_c2_frigate_desc", "The Victory-II Frigate is extensively used by the Empire ^due to its heavy support capabilities."),
  ("spaceship_imperial_trade_frigate_name", "Imperial Trade Frigate"),
  ("spaceship_imperial_trade_frigate_desc", "The standard Imperial Trade Frigate has a decent base speed ^and lots of space for either troops or cargo."),
  ("spaceship_tie_fighter_name", "Imperial Tie Fighter"),
  ("spaceship_tie_fighter_desc", "The Tie Fighter is a relatively modern fighter that makes use of ^the last propulsion technology."),
  ("spaceship_imperial_shuttle_name", "Lambda-class T-4a Shuttle"),
  #("spaceship_imperial_shuttle_desc", "A true beauty, the Imperial Shuttle combines speed with troop support capabilites. ^^It has one troop compartment with room for two more and a MK-I Medical bay ^which can be upgraded to MK-II. ^^The current MK-I scanners could be upgraded to MK-III if you require a larger scanning range."),
  ("spaceship_imperial_shuttle_desc", "A true beauty, the Lambda Shuttle combines speed ^with troop support capabilites."),
  #rebel
  ("spaceship_a_wing_name", "A-Wing"),
  ("spaceship_a_wing_desc", "The A-Wing is the most maneuverable fighter in the galaxy. ^It's very fast and totally reliable."),
  ("spaceship_rebel_transport_name", "GR-75 Medium Transport"),
  #("spaceship_rebel_transport_desc", "The Rebel Cruiser is a sleek and highly sophisticated battleship ^^Your troops will be carried in the two to four troop compartments and will be ^transported swiftly to their destination by the MK-II engines, upgradable to MK-IV. ^^The ship offers extensive medical facilites from the standard MK-II MedBay, up to ^a fully equiped hospital at MK-V. ^^The rebels build the most powerful scanners and combat computers available today. ^Both come standard at MK-II but can be upgraded to MK-V."),
  ("spaceship_rebel_transport_desc", "The Gallofree Medium Transport is an excellent armored transport."),
  ("spaceship_moncal_cruiser_name", "Mon Cal Cruiser"),
  ("spaceship_moncal_cruiser_desc", "The Mon Calamari Cruiser fields good weaponry ^among with the best shielding technology."),  
  ("spaceship_corellian_gunship_name", "DP20 Frigate"),
  ("spaceship_corellian_gunship_desc", "The Corellian Gunship is fast and very well equiped for it's size."),  
  ("spaceship_corellian_corvette_name", "CR90 Corvette"),
  ("spaceship_corellian_corvette_desc", "The Corellian Corvette is a very fast ship, and great for battle light support."),  
  ("spaceship_x_wing_name", "X-Wing"),
  ("spaceship_x_wing_desc", "The emblem of the Rebels, the X-Wing it's a well known lightspeed dogfighter, expertise in fast combat across the galaxy."),  
  ("spaceship_y_wing_name", "Y-Wing"),
  ("spaceship_Y_wing_desc", "Though its design is a little outdated it's a decent match for fighters ^and a fearsome bomber."),  
  #hutt
  ("spaceship_hutt_cruiser_name", "Hutt Cruiser"),
  ("spaceship_hutt_cruiser_desc", "The standard MK-1 Hutt Cruiser is a very versatile ship."),
  ("spaceship_hutt_frigate_mk1_name", "Hutt MK-1 Frigate"),
  ("spaceship_hutt_frigate_mk1_desc", "The standard Hutt Cruiser is good as armored transport."),
  ("spaceship_hutt_frigate_mk2_name", "Hutt MK-2 Frigate"),
  ("spaceship_hutt_frigate_mk2_desc", "The standard MK-2 Frigate is great for troop transport ^while being quite versatile."),
  ("spaceship_hutt_trade_name", "Hutt Trade Ship"),
  ("spaceship_hutt_trade_desc", "Though quite slow, the standard Hutt Trade Ship makes use ^of an excellent trade computer and cargo hold."),
  ("spaceship_hutt_patrol_name", "Hutt Patrol Ship"),
  ("spaceship_hutt_patrol_desc", "The standard Hutt Patrol Ship is excellent for tracking transports ^on short distances."),
  #other
  ("spaceship_z95_name", "Z-95 HeadHunter"),
  #("spaceship_z95_desc", "The z-95 Headhunter is a fast and agile craft which will see you safely to ^all corners of the galaxy. ^^Its powerful MK-III engines can be upgraded to MK-V to make it the fastest ^ship out there, unless you believe that nonsense about the Millenium Falcon.^^It has MK-I scanners with the option to upgrade to MK-III."),
  ("spaceship_z95_desc", "The z-95 Headhunter is a fast and agile craft which will take you safely to ^all corners of the galaxy."),
  ("spaceship_scyk_fighter_name", "M3-A Scyk Fighter"),
  ("spaceship_scyk_fighter_desc", "Fast and capable of defending itself, the Scyk fighter can handle ^any situation a normal traveller might face."),
#  ("spaceship_mercenary_raider_name", "Mercenary Raider"), <- now Wild Karrde
  ("spaceship_mercenary_raider_name", "Wild Karrde"),
  #("spaceship_mercenary_raider_desc", "The Mercenary Raider is an all-round winner. ^^While already no slouch, it can be made faster still with drive upgrades. ^There is plenty of room for detaining defeated enemies with room for ^two additional compartments if required.^^Enhanced scanners help detect enemies while the MK-I Combat Computer ^will give you the edge in any fight. ^If you still find yourself on the losing end, you can upgrade to a MK-III model."),  
  ("spaceship_mercenary_raider_desc", "Very good prisoner capacity and base speed. A good choice ^for bountyhunters or small mercenenary groups."),  
  ("spaceship_freighter_name", "Freighter"),
  #("spaceship_freighter_desc", "This model Freighter is the workhorse of traders around the galaxy. ^^Its basic engines are somewhat outdated but can easily be upgraded to MK-III.^^The ship has a pressurized cargo hold with room for four additional units to be installed. ^^The MK-I trade computer will make sure you get a fair price but if you ^really want to hunt for the sharpest deal, you can uprade to a MK-V model. ^^There is also room for two prisoner comparments, with one already installed."),
  ("spaceship_freighter_desc", "This standard Freighter is the workhorse of traders around the galaxy."),
  ("spaceship_mercenary_fighter_name", "T-Wing interceptor"),
  ("spaceship_mercenary_fighter_desc", "A respectful combination of good weaponry and powerful drives"),
  ("spaceship_mercenary_shuttle_name", "Mercenary Shuttle"),
  ("spaceship_mercenary_shuttle_desc", "The standard mercenary shuttle isn't designed for intense combat, ^but it's quite fast and versatile."),
  ("spaceship_civilian_transport_name", "Civilian Transport"),
  ("spaceship_civilian_transport_desc", "With enough space for a small party this ship can take you ^around the galaxy with a good speed."),
  ("spaceship_civilian_cruiser_name", "Civilian Cruiser"),
  ("spaceship_civilian_cruiser_desc", "Though it's slow, the standard Civilian Cruiser can be ^very useful as medium transport"),  
  ("spaceship_bulk_freighter_name", "Bulk Freighter"),
  ("spaceship_bulk_freighter_desc", "Though slow and barely armed, the Bulk Freighter ^is the perfect transport for commercial purposes."),
  ("spaceship_cis_star_cruiser_name", "Lucrehulk-class Battleship"),
  ("spaceship_cis_star_cruiser_desc", "Though initially designed as a heavy transport, the Lucrehulk-class ship ^is multipurpose and perfectly defends itself."),
  ("spaceship_nebulon_name", "EF76 Nebulon-B Frigate"),
  ("spaceship_nebulon_desc", "Designed as an anti-starfighter battleship, the Nebulon Frigate^is great for escorting, but can be also converted into medical ship."), 
  ("spaceship_starchaser_name", "R-41 Starchaser Fighter"),
  ("spaceship_starchaser_desc", "Though outdated already for the Galactic Civil War this fighter has powerful drives and good weaponry."),   
  
  
#SW - spaceship string ends
  ("swy_space_battles_won", "-Victory-"),
  ("swy_space_battles_won_desc", "Congratulations, commander^You have won the battle..."),
  
  
# swconquest 1.011 -- in-game credits
  ("swconquest_credits_years",'2008-'+str(datetime.now().year)+' THE STAR WARS CONQUEST DEV TEAM^'+ #-> from now on the year changes automatically.
                              '<http://getconquest.net>'),
                              
  ("swconquest_credits_prefc",'This module is dedicated to everyone who believed in our team.^'+
                              'Their valuable support has inspired us to make this even bigger.^^'+
                              
                              'Patience is always rewarded.'),
                              
  ('swconquest_credits_contb','Original Programming and Development:^'+
                              ' Brian Tommasini <HokieBT>^^'+

                              'Main Programming and Coordinator:^'+
                              ' Ismael Ferreras^^'+

                              'Senior Modeling and Contributors:^'+
                              ' Tim Ramsay^'+
                              ' Yiyang Chen^'+
                              ' Daniel Harrington^'+
                              ' Josh <HappyStormTrooper>^'+
                              ' Marosh <Geroj>^^'+

                              'Music Composition and Performance:^'+
                              ' Vladan Zivanovic^'+
                              ' (www.DarkRuneCreations.com.au)^^'+

                              'Additional AI Programming:^'+
                              ' Michael Richter^^'+

                              'Additional Gameplay Programming:^'+
                              ' Martin F.^^'+

                              'Original Artwork and Conceptualization:^'+
                              ' Giordano Pranzoni^'+
                              ' Benjamin Carré^^'+

                              'Scene Editing:^'+
                              ' Tim Ramsay^'+
                              ' Miguel Angel Centeno^^^^'+
                              
                              

                              'Additional Modeling:^'+
                              ' Dustin Matthew Blamey^'+
                              ' Sam <uio0000>^'+
                              ' <Zahar>^'+
                              ' <HapSlash>^'+
                              ' <Grocat>^'+
                              ' <LordOfTheSithLords>^'+
                              ' <Highelf>^'+
                              ' <Takijap>^'+
                              ' <Thorgils>^'+
                              ' <WookiePadawan>^'+
                              ' <Tyrinius>^'+
                              ' <Freddex>^^'+

                              'Our best gratitude to the Old Team:^'+
                              ' Brian, Tim, Josh and Marosh^^'+

                              'Special Thanks:^'+
                              ' Marco Tarini <mtarini> - OpenBRF is our cornerstone^'+
                              ' Jack <Mechwarrior24>, Alex <Panda666>, Cyrano7,^'+
                              ' TheStarWarsGuru and airtroop392 - Dialog modernizers and proofreaders^'+
                              ' Luke Challand  <ithilienranger> – For the annoying questions^'+
                              ' Scott Reismanis <INtense!> – ModDB is a better place^'+
                              ' Creators of the included mods, code snippets and enhancements – 1866,^'+
                              ' Gangs of Glasgow, Mount&Shotgun, MAXHARDMAN, Rubik, Gutekfiutek, hapslash...^^'+

                              ' To all our fans and supporters, may the force be with you, always.'),

  ("cmenu_follow", "Accompany"),
]
