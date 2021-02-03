#!/usr/bin/env python3

class contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class lead:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone




ContactList = []

ContactList.append(contact('Alice Brown', '', '1231112223'))
ContactList.append(contact('Bob Crown', 'bob@crowns.com', ''))
ContactList.append(contact('Carlos Drew', 'carl@drewess.com', '3453334445'))
ContactList.append(contact('Doug Emerty', '', '4564445556'))
ContactList.append(contact('Egan Fair', 'eg@fairness.com', '5675556667'))


LeadList = []

LeadList.append(lead('', 'kevin@keith.com', ''))
LeadList.append(lead('Lucy', 'lucy@liu.com', '3210001112'))
LeadList.append(lead('Mary Middle', 'mary@middle.com', '3331112223'))
LeadList.append(lead('', '', '4442223334'))
LeadList.append(lead('', 'ole@olson.com', ''))


registrants = [
{
  "registrant":
     {
        "name": "Lucy Liu",
        "email": "lucy@liu.com",
        "phone": "",
     }
},
{
  "registrant":
     {
        "name": "Doug",
        "email": "doug@emmy.com",
        "phone": "4564445556",
     }
},
{
  "registrant":
     {
        "name": "Uma Thurman",
        "email": "uma@thurs.com",
        "phone": "",
     }
}
]

for reg in registrants:
    match = False
    for c in ContactList:
        if reg['registrant']['email'] == c.email and reg['registrant']['email'] != '':
            ContactList = [x for x in ContactList if (reg['registrant']['email'] != x.email)]
            match = True
        elif reg['registrant']['phone'] == c.phone and reg['registrant']['phone'] != '':
            ContactList = [x for x in ContactList if (reg['registrant']['phone'] != x.phone)]
            match = True

        if match:
            ContactList.append(contact(reg['registrant']['name'], reg['registrant']['email'], reg['registrant']['phone']))
            break
        else:
            for l in LeadList:
                if (reg['registrant']['email'] == l.email and reg['registrant']['email'] != ''):
                    ContactList = [x for x in ContactList if not (reg['registrant']['email'] == x.email)]
                    LeadList = [x for x in LeadList if not (reg['registrant']['email'] == x.email)]
                    ContactList.append(contact(reg['registrant']['name'], reg['registrant']['email'], reg['registrant']['phone']))
                elif reg['registrant']['phone'] == l.phone and reg['registrant']['phone'] != '':
                    ContactList = [x for x in ContactList if not (reg['registrant']['phone'] == x.phone)]
                    LeadList = [x for x in LeadList if not (reg['registrant']['phone'] == x.phone)]
                    ContactList.append(contact(reg['registrant']['name'], reg['registrant']['email'], reg['registrant']['phone']))
                else:
                    ContactList.append(contact(reg['registrant']['name'], reg['registrant']['email'], reg['registrant']['phone']))
        ContactList.append(contact(reg['registrant']['name'], reg['registrant']['email'], reg['registrant']['phone']))


print('\nAssistants')
for c in ContactList:
    print(str(c.name), str(c.email), str(c.phone))

print('\nLeads')
for l in LeadList:
    print(str(l.name), str(l.email), str(l.phone))