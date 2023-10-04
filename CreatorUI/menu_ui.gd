extends Control

@onready var menu_control = $MenuButton

enum MenuIDs {
	CHAR_LOAD,
	CHAR_SAVE,
	DATA_MANAGE,
	ABOUT,
	EXIT
}


# Called when the node enters the scene tree for the first time.
func _ready():
	var popup = menu_control.get_popup()
	popup.add_item("Load Character", MenuIDs.CHAR_LOAD)
	popup.add_item("Save Character", MenuIDs.CHAR_SAVE)
	popup.set_item_disabled(MenuIDs.CHAR_SAVE,true)
	popup.add_item("Data Management", MenuIDs.DATA_MANAGE)
	popup.add_item("About", MenuIDs.ABOUT)
	popup.add_item("Exit", MenuIDs.EXIT)
	popup.id_pressed.connect(_on_item_menu_pressed)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func _on_item_menu_pressed(id):
	print("Menu Click: ",id)
	match id:
		MenuIDs.CHAR_LOAD:
			print("load a character")
		MenuIDs.CHAR_SAVE:
			print("save the loaded character")
		MenuIDs.DATA_MANAGE:
			print("manage data")
		MenuIDs.ABOUT:
			print("about window")
			$AcceptDialog.popup()
		MenuIDs.EXIT:
			get_tree().quit()