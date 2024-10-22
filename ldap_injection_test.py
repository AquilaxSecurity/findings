import ldap

def vulnerable_ldap_query(user_input):
    conn = ldap.initialize('ldap://localhost')
    base_dn = "ou=users,dc=example,dc=com"
    
    # Vulnerable to LDAP Injection
    search_filter = "(uid=" + user_input + ")"
    
    conn.search(base_dn, ldap.SCOPE_SUBTREE, search_filter)
