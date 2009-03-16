#!/www/python/bin/python

"""
Test script for jwzthreading.

"""
import unittest
import email
import jwzthreading


class JWZTest(unittest.TestCase):
    def test_container(self):
        c = jwzthreading.Container()
        c2 = jwzthreading.Container()
        self.assertTrue(c.is_dummy())
        self.assertEqual(c.children, [])
        self.assertEqual(c.parent, None)
        self.assertFalse(c.has_descendant(c2))

        # Add a child
        c3 = jwzthreading.Container()
        c.add_child(c2)
        c2.add_child(c3)
        self.assertEqual(c.children, [c2])
        self.assertEqual(c2.parent, c)
        self.assertTrue(c.has_descendant(c2))
        self.assertTrue(c.has_descendant(c3))

        # Remove a child
        c.remove_child(c2)
        self.assertEqual(c.children, [])
        self.assertEqual(c2.parent, None)
        self.assertFalse(c.has_descendant(c3))
        self.assertTrue(c2.has_descendant(c3))

    def test_make_message (self):
        msg_templ = """Subject: %(subject)s
Message-ID: %(msg_id)s

Message body
"""
        m = email.message_from_string("""Subject: random

Body.""")
        self.assertRaises(ValueError, jwzthreading.make_message, m)

if __name__ == "__main__":
    unittest.main()
