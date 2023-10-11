extends Control

@onready var bond_name:LineEdit = $BondMarginContainer/HBoxContainer/BondName

@onready var admiration_box:CheckBox = $BondMarginContainer/HBoxContainer/VBoxContainer/Admiration
@onready var inferiority_box:CheckBox = $BondMarginContainer/HBoxContainer/VBoxContainer/Inferiority

@onready var loyalty_box:CheckBox = $BondMarginContainer/HBoxContainer/VBoxContainer2/Loyalty
@onready var mistrust_box:CheckBox = $BondMarginContainer/HBoxContainer/VBoxContainer2/Mistrust

@onready var affection_box:CheckBox = $BondMarginContainer/HBoxContainer/VBoxContainer3/Affection
@onready var hatred_box:CheckBox = $BondMarginContainer/HBoxContainer/VBoxContainer3/Hatred

func export():
	var dict = {
		'name': bond_name.text,
		'admiration': admiration_box.button_pressed,
		'inferiority': inferiority_box.button_pressed,
		'loyalty': loyalty_box.button_pressed,
		'mistrust': mistrust_box.button_pressed,
		'affection': affection_box.button_pressed,
		'hatred': hatred_box.button_pressed
	}
	return dict

func import(dict):
	bond_name.text = dict['name']
	admiration_box.button_pressed = dict['admiration']
	inferiority_box.button_pressed = dict['inferiority']
	loyalty_box.button_pressed = dict['loyalty']
	mistrust_box.button_pressed = dict['mistrust']
	affection_box.button_pressed = dict['affection']
	hatred_box.button_pressed = dict['hatred']
	


func _on_admiration_pressed():
	inferiority_box.disabled = admiration_box.button_pressed


func _on_inferiority_pressed():
	admiration_box.disabled = inferiority_box.button_pressed


func _on_loyalty_pressed():
	mistrust_box.disabled = loyalty_box.button_pressed


func _on_mistrust_pressed():
	loyalty_box.disabled = mistrust_box.button_pressed


func _on_affection_pressed():
	hatred_box.disabled = affection_box.button_pressed


func _on_hatred_pressed():
	affection_box.disabled = hatred_box.button_pressed
