# DrawTree

By Mathieu Guillame-bert
21 Oct. 2016

## Description

This script draws a tree (in text mode) front of a set of tabulated text file.

## Example

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

Becomes

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
  
