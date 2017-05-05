# DrawTree

By Mathieu Guillame-bert
achoum@gmail.com

## Description

DrawTree is a command line tool used to augment recursive lists (i.e. trees).

## Example

Input:

```
DoAny
	EatSomeFood [extends DoAll]
		EnsureItemInInventory(x,y=Food) [extends DoAny]
			HasItemInInventory(x,y)
			GetReachableItemFromGround(x,y) [extends DoAll]
				FindReachableItemOnGround(x,y)
				Goto(x)
				Grab(x)
			GetReachableItemFromContainer(x,y) [extends DoAll]
				FindReachableItemInContainer(x,y,z)
				Goto(z)
				GrabFromContainer(x,z)
		Eat(x)
	RandomWalk
```

Output:

```
DoAny
  |
  +--EatSomeFood [extends DoAll]
  |    |
  |    +--EnsureItemInInventory(x,y=Food) [extends DoAny]
  |    |    |
  |    |    +--HasItemInInventory(x,y)
  |    |    +--GetReachableItemFromGround(x,y) [extends DoAll]
  |    |    |    |
  |    |    |    +--FindReachableItemOnGround(x,y)
  |    |    |    +--Goto(x)
  |    |    |    +--Grab(x)
  |    |    +--GetReachableItemFromContainer(x,y) [extends DoAll]
  |    |         |
  |    |         +--FindReachableItemInContainer(x,y,z)
  |    |         +--Goto(z)
  |    |         +--GrabFromContainer(x,z)
  |    +--Eat(x)
  +--RandomWalk
```

Command line example:

```
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
```

## Options

There is currently command line options. Instead, the options are modifiable by editing various constants defined at the top of the script.

These options are:

- END_BRANCH: What to print in front of the last child (default: "  +--")
- INTERM_BRANCH: What to print in front of a child (which is not the last child) (default: "  +--")
- CONTINUITY: What to print to extand a branch (default:"  |  ")
- NOTHING: What to print when there is nothing (default:"     ")
- ADD_SPACE: Should we skip a blank line between a node and its first child (default:True).
