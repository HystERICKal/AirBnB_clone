#!/usr/bin/python3

import cmd
import models
import sys
from shlex import split as split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

the_classes = {'BaseModel': BaseModel, 'Review': Review, 'User': User,
               'State': State, 'Amenity': Amenity, 'Place': Place,
               'City': City}


class HBNBCommand(cmd.Cmd):
    """The CLI"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exit program"""
        return SystemExit

    def do_EOF(self, line):
        """ ctrl+d """
        print()
        return True

    def emptyline(self):
        """ Nothing """
        pass

    def do_create(self, line):
        """new instance creation"""
        split_to_list = split(line)
        if not split_to_list:
            print("** class name missing **")
        elif split_to_list[0] not in the_classes:
            print("** class doesn't exist **")
        else:
            fresh_user = the_classes[split_to_list[0]]()
            print(fresh_user.id)
            fresh_user.save()

    def do_show(self, line):
        """string rep"""
        if not line:
            print("** class name missing **")
        elif line.split()[0] not in the_classes.keys():
            print("** class doesn't exist **")
        elif len(line.split()) < 2:
            print("** instance id missing **")
        else:
            fresh_user = "{}.{}".format(line.split()[0], line.split()[1])
            temp = models.storage.all()

            if fresh_user not in temp:
                print("** no instance found **")
            else:
                print(temp[fresh_user])

    def do_destroy(self, line):
        """instance deletion"""
        split_to_list = split(line)

        if not split_to_list:
            print("** class name missing **")
            return False

        elif split_to_list[0] not in the_classes:
            print("** class doesn't exist **")

        elif len(split_to_list) < 2:
            print("** instance id missing **")

        else:
            fresh_user = split_to_list[0] + '.' + split_to_list[1]
            if fresh_user not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[fresh_user]
                models.storage.save()

    def do_all(self, line):
        """string rep"""
        temp_list = []

        if not line:
            for fresh_user in models.storage.all().values():
                temp_list.append(str(fresh_user))
        else:
            split_to_list = split(line)
            if split_to_list[0] in the_classes:
                for j, i in models.storage.all().items():
                    if i.__class__.__name__ == split_to_list[0]:
                        temp_list.append(str(i))
            else:
                print("** class doesn't exist **")
                return False
        print(temp_list)

    def do_update(self, line):
        """instance update"""
        split_to_list = split(line)

        if not split_to_list:
            print("** class name missing **")

        elif split_to_list[0] not in the_classes:
            print("** class doesn't exist **")

        elif len(split_to_list) < 2:
            print("** instance id missing **")

        elif len(split_to_list) < 3:
            print("** attribute name missing **")

        elif len(split_to_list) < 4:
            print("** value missing **")

        else:
            fresh_user = split_to_list[0] + '.' + split_to_list[1]
            if fresh_user not in models.storage.all():
                print("** no instance found **")
            else:
                setattr(models.storage.all()[fresh_user],
                        split_to_list[2], split_to_list[3])
                models.storage.save()

    def default(self, line):
        """the default method"""
        tallyy = 0
        split_to_list = line.split('.', 1)
        if len(split_to_list) >= 2:
            line = split_to_list[1].split('(')
            if line[0] == 'all':
                self.do_all(split_to_list[0])
            elif line[0] == 'count':
                for tr in models.storage.all():
                    if split_to_list[0] == tr.split(".")[0]:
                        tallyy += 1
                print(tallyy)
            elif line[0] == 'show':
                temp_id = line[1].split(')')
                sent_id = str(split_to_list[0]) + " " + str(temp_id[0])
                self.do_show(sent_id)
            elif line[0] == 'destroy':
                temp_id = line[1].split(')')
                sent_id = str(split_to_list[0]) + " " + str(temp_id[0])
                self.do_destroy(sent_id)
            elif line[0] == 'update':
                sasisha = line[1].split(')')
                gawanya = sasisha[0].split('{')
                if len(gawanya) == 1:
                    line = sasisha[0].split(",")
                    sent_id = str(split_to_list[0]) + " " + str(line[0]) + \
                        " " + str(line[1]) + " " + str(line[2])
                    self.do_update(sent_id)
                else:
                    temp_id = gawanya[0][:-2]
                    sent_dict = gawanya[1][:-1]
                    seprtor = sent_dict.split(',')
                    for g in seprtor:
                        temp_vall = g.split(':')
                        sent_id = str(split_to_list[0]) + " " + \
                            str(temp_id) + " " + str(temp_vall[0]) + \
                            " " + str(temp_vall[1])
                        self.do_update(sent_id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
