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
