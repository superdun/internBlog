# encoding=utf-8
import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import dbORM as db


def get_info(msg):

    user = decode_str(msg.get('From', ''))
    hdr, addr = parseaddr(user)
    name = decode_str(hdr)
    user = u'%s' % name
    date = decode_str(msg.get('Date', ''))
    if (msg.is_multipart()):

        parts = msg.get_payload()
        for n, part in enumerate(parts):
            if part.get_content_type() == 'text/plain':
                content = part.get_payload(decode=True)

                charset = guess_charset(msg)
                if charset:
                    content = content.decode(charset)
                break
            else:
                content = 'error'

    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
        else:
            content = 'error'
    return {'username': user, 'date': date, 'content': content}


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):

    charset = msg.get_charset()
    if charset is None:

        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def store_to_db(info):

    have_user = db.session.query(db.Users).filter_by(
        name=info['username']).all()
    if len(have_user) == 0:
        db.session.add(db.Users(name=info['username']))
        db.session.commit()
    have_post = db.session.query(db.Posts).filter(db.and_(db.Posts.date==info['date'],db.Posts.title==info['username'])).all()
    if len(have_post) != 0:
        return 'UPTODATE'
    db.session.add(db.Posts(body=info['content'], date=info['date'], status='published', title=info[
                   'username'], authorId=db.session.query(db.Users).filter_by(name=info['username']).one().id))
    db.session.commit()
    db.session.close()
    return 'CONTINUE'
if __name__ == "__main__":
    email = "lidun@wallstreetcn.com"
    password = 'Qw96163'
    pop3_server = 'pop.exmail.qq.com'

    server = poplib.POP3(pop3_server)

    print(server.getwelcome())

    server.user(email)
    server.pass_(password)
    posts_amount, size = server.stat()

    resp, mails, octets = server.list()
    msg_list = []
    # print(mails)
    for i in range(1, len(mails) + 1):
        print 'reading email list %d/%d' % (i, posts_amount)
        resp, lines, octets = server.retr(i)
        msg_content = '\r\n'.join(lines)
        msg = Parser().parsestr(msg_content)
        info = get_info(msg)
        if store_to_db(info) == 'UPTODATE':
            i = len(mails) + 1
        print '%d/%d done' % (i, posts_amount)
    server.quit()
