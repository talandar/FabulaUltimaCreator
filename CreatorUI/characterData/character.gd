class_name Character

var fileLoc = null
var namePronouns = ""
var identity = ""
var theme = ""
var origin = ""

var bonds: Array[Bond]

var fabulaPoints = 0
var experiencePoints = 0

var initMod = ""
var defense = ""
var magDefense = ""

var equip_martial_armor = false
var equip_martial_shield = false
var equip_martial_melee = false
var equip_martial_ranged = false

var mainHand:EquipItem = null






func save(path):
	print("TODO save to ",fileLoc)
	
func load(path):
	print("TODO load from ",fileLoc)
