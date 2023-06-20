from view import menu,show_contacts,print_message,input_contact,input_return
import model
from view import text

def start():
    while True:
        choice = menu()
        match choice:
            case 1:
                model.open_file()
                print_message(text.open_successful)
            case 2:
                pass
            case 3:
                show_contacts(model.phone_book)
            case 4:
                new = input_contact(text.input_new_contact)
                model.add_contact(new)
                print_message(text.contact_saved(new.get('name')))
            case 5:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
            case 6:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
                index = input_return(text.input_index)
                new = input_contact(text.input_change_contact)
                model.change(int(index),new)
                old_name = model.phone_book[int(index)-1].get('name')
                print_message(text.contact_changed(new.get('name')if new.get('name')else old_name))
            case 7:
                name = input_return(text.input_name)
                contact_index = model.get_contact_index_by_name(name)
                if contact_index is not None:
                    new = input_contact(text.input_change_contact)
                    model.change(contact_index,new)
                    old_name = model.phone_book[contact_index].get('name')
                    print_message(text.contact_changed(new.get('name')if new('name')else old_name))
                else:
                    print_message('Contact with name "{}" not found.'.format(name))
            case 8:
                name = input_return(text.input_name)
                contact_index = model.get_contact_index_by_name(name)
                if contact_index is not None:
                    model.delete_contact(contact_index)
                    print_message('Contact "{}" has been deleted.'.format(name))
                else:
                    print_message('Contact with name "{}" not found.'.format(name))
            case 9:
                break







