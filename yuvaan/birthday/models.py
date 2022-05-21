from django.db import models
from django.db import connection
from ..rsvp.models import dict_fetchall
# Create your models here.


def get_guest_by_id(guest_id):
    data = []
    sql = """
                    SELECT `guests`.`guest_id`,
                        `guests`.`invitee`,
                        `guests`.`phone`,
                        `guests`.`kids_expected`,
                        `guests`.`adults_expected`,
                        `guests`.`status`
                    FROM `yuvaan`.`guests`
                    where guest_id = %(guest_id)s


            """
    with connection.cursor() as cursor:
        cursor.execute(sql, {'guest_id': guest_id})
        out = dict_fetchall(cursor)
        cursor.close()
    if len(out):
        data = out[0]
    return data


def register_rsvp(fields):
    sql = """
    INSERT INTO `yuvaan`.`rsvp`
    (
    `guest_id`,
    `adults`,
    `kids`,
    `status`
    )
    VALUES
    (
    %(guest)s,
    %(adults)s,
    %(kids)s,
    %(status)s
    )
    """

    with connection.cursor() as cursor:
        cursor.execute(sql, fields)
        cursor.close()

    return fields['guest']
