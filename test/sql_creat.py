user_id = 26286
file = 'subreportidlist.txt'

content = ''


def write_string_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


file_path = 'output2.txt'

with open(file, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        sql = f"insert into gnomon_user_resources (user_id, privilege_id, resource_id, can_copy, can_download, operater, operate_way, is_delete) values ({user_id}, 2, {line}, 1, 1, 'admin', 0, 0);"
        print(sql)
        content += sql + '\n'

write_string_to_file(file_path, content)
