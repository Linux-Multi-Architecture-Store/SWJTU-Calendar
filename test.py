import core.ics.main as ics


x = ics.Ics()
x.create_task(
    [
        "name1", "2022", "071300", "081200", "0913", "place"
    ]
)
x.create_task(
    [
        "name2", "2022", "091300", "101200", "0913", "place"
    ]
)
x.generate_data_dict()
x.save_file()