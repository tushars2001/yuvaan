from django.db import connection
import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your models here.


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_all_rsvp():
    data = []
    sql = """
            SELECT `rsvp`.`rsvpid`,
            `rsvp`.`guest_id`,
            `rsvp`.`adults`,
            `rsvp`.`kids`,
            `rsvp`.`status`,
            guests.invitee as guest_name from
            yuvaan.rsvp rsvp, yuvaan.guests guests
            where guests.guest_id = rsvp.guest_id;

    """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        data = dict_fetchall(cursor)
        cursor.close()

    return data


def get_all_invitations():
    data = []
    sql = """
                SELECT `guests`.`guest_id`,
                    `guests`.`invitee`,
                    `guests`.`phone`,
                    `guests`.`kids_expected`,
                    `guests`.`adults_expected`,
                    `guests`.`status`
                FROM `yuvaan`.`guests`;


        """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        data = dict_fetchall(cursor)
        cursor.close()

    return data


def get_rsvp_by_guest_id(guest_id):
    data = []
    sql = """
                SELECT `rsvp`.`rsvpid`,
                `rsvp`.`guest_id`,
                `rsvp`.`adults`,
                `rsvp`.`kids`,
                `rsvp`.`status`,
                guests.invitee as guest_name from
                yuvaan.rsvp rsvp, yuvaan.guests guests
                where guests.guest_id = rsvp.guest_id
                and guests.guest_id = %(guest_id)s
                order by rsvpid desc
                limit 1

        """
    with connection.cursor() as cursor:
        cursor.execute(sql, {'guest_id': guest_id})
        data = dict_fetchall(cursor)
        cursor.close()

    return data

