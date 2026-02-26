def test_conflict_logic():

    existing_start = 10
    existing_end = 11

    new_start = 10.5
    new_end = 11.5

    conflict = new_start < existing_end and new_end > existing_start

    assert conflict == True