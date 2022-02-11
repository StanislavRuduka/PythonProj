class Editor:
    license_key = '3647-8947'

    def view_document(self):
        return 'You are viewing a document'

    def edit_document(self):
        return 'Editing is unavailable for free version'


class ProEditor(Editor):

    def edit_document(self):
        return 'You are now able to edit'


key = input('Input the license key: ')
if key != Editor.license_key:
    noEdit = Editor()
    print(noEdit.edit_document())
else:
    yesEdit = ProEditor()
    print(yesEdit.edit_document())
