class_name CharacterSheet extends Control

@onready var name_text_field = $MarginContainer/Topbar/NameText
@onready var pronouns_text_field = $MarginContainer/Topbar/PronounsText
@onready var bonds_container = find_child("BondsContainer",true,false)
@onready var attributes = $ScrollContainer/ScrollItems/AttrPanel/Attributes

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
	pass


func _on_menu_button_save_called():
	print("save called")
	var dict = {
		"name": name_text_field.text,
		"pronouns": pronouns_text_field.text,
		"attributes": attributes.export(),
		"bonds": _get_bond_export()
	}
	print(dict)
	
func _get_bond_export():
	var box_1 = bonds_container.get_child(0)
	var bond_0 = box_1.get_child(0)
	var bond_1 = box_1.get_child(1)
	var bond_2 = box_1.get_child(2)
	var box_2 = bonds_container.get_child(1)
	var bond_3 = box_2.get_child(0)
	var bond_4 = box_2.get_child(1)
	var bond_5 = box_2.get_child(2)
	return [bond_0.export(),bond_1.export(),bond_2.export(),bond_3.export(),bond_4.export(),bond_5.export()]
	
