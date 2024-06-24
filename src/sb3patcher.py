from json import load, dump


def lockbreaker_patch(parent, next1):
    return {
          "opcode": "data_setvariableto",
          "next": next1,
          "parent": parent,
          "inputs": {
            "VALUE": [
              1,
              [
                10,
                "Off"
              ]
            ]
          },
          "fields": {
            "VARIABLE": [
              "LoginScr",
              "gy3e#m$5c{#~Il!57X(Z"
            ]
          },
          "shadow": False,
          "topLevel": False
        }


def patchProjectJSON(filepath: str) -> None:
    # List of sprites that may potentially trigger the anticheat
    n7r_patch = {
          "opcode": "event_whenflagclicked",
          "next": "lockbreakerpatch0000",
          "parent": None,
          "inputs": {},
          "fields": {},
          "shadow": False,
          "topLevel": True,
          "x": -638,
          "y": -2417,
          "comment": "HF9G+o|:va@Nm)jf=))("
        }
    culprit_sprites = [
        'Terminal.mx',
    ]
    culprit_ids = [
        'N{[7R):=.se|I!l!`!FW',
    ]
    culprit_edit_parent = [
        '9w_[~`$!7yr+vW5O9:)=',
    ]

    with open(filepath, "r") as f:
        try:
            project = load(f)
            sprites = project['targets']
            print("Browsing project.json.")
        except TypeError:
            print(f"[ERROR] Could not load project.json! Are you sure '{filepath}' is the right file path?")

    if type(project) == dict:
        for i in sprites:
            if i['name'] in culprit_sprites:
                print(f"Culprit found: `{i['name']}`. Finding exploit area.")
                for block in i['blocks']:
                    if block in culprit_ids:
                        i['blocks'][block] = n7r_patch
                        culprit_id_parent = block
                    if block in culprit_edit_parent:
                        i['blocks'][block]['parent'] = "lockbreakerpatch0000"
                        culprit_id_next = block
                print("Patched sprite pointers, adding patch block...")
                i['blocks'].update({"lockbreakerpatch0000": lockbreaker_patch(culprit_id_parent, culprit_id_next)})
        project['targets'] = sprites
        with open(filepath, "w") as f:
            print("Saving project.json...")
            dump(project, f, indent=None)
    else:
        print("[ERROR] Could not recognize file structure.")