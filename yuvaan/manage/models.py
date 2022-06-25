import pdb

from django.db import models
from django.db import connection
from ..rsvp.models import dict_fetchall


def add_guest(fields):
    sql = """
               INSERT INTO `yuvaan`.`guests`
            (
            `guest_id`,
            `invitee`,
            `phone`,
            `kids_expected`,
            `adults_expected`
            )
            VALUES
            (
            %(guest_id)s,
            %(invitee)s,
            %(phone)s,
            %(kids_expected)s,
            %(adults_expected)s
            );

        """
    with connection.cursor() as cursor:
        cursor.execute(sql, fields)
        cursor.close()

    return True


def update_guest(fields):
    sql = """
               UPDATE `yuvaan`.`guests`
            SET
            `guest_id` = %(guest_id)s,
            `invitee` = %(invitee)s,
            `phone` = %(phone)s,
            `kids_expected` = %(kids_expected)s,
            `adults_expected` = %(adults_expected)s,
            `status` = %(status)s
            WHERE `guest_id` = %(guest_id)s;

        """
    with connection.cursor() as cursor:
        cursor.execute(sql, fields)
        cursor.close()
    return True


def get_all_messages():
    sql = """
    select g.invitee as name, g.guest_id, concat('https://api.whatsapp.com/send/?phone=1',g.phone,'&text=We%20invite%20you%20to%20Yuvann%27s%20Birthday.%20Details%20and%20RSVP%20here:%20https://yuvaan.world/turning-1/?guest=',g.guest_id,'&app_absent=0') link
 , r.status from guests g left join rsvp r on r.guest_id=g.guest_id and r.active=1
 order by r.status, g.invitee"""

    with connection.cursor() as cursor:
        cursor.execute(sql)
        data = dict_fetchall(cursor)
        cursor.close()
    return data
