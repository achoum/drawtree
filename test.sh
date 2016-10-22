echo -e "DoAny \n\
	EatSomeFood [extends DoAll] \n\
		EnsureItemInInventory(x,y=Food) [extends DoAny] \n\
			HasItemInInventory(x,y) \n\
			GetReachableItemFromGround(x,y) [extends DoAll] \n\
				FindReachableItemOnGround(x,y) \n\
				Goto(x) \n\
				Grab(x) \n\
			GetReachableItemFromContainer(x,y) [extends DoAll] \n\
				FindReachableItemInContainer(x,y,z) \n\
				Goto(z) \n\
				GrabFromContainer(x,z) \n\
		Eat(x) \n\
	RandomWalk" | python drawtree.py
