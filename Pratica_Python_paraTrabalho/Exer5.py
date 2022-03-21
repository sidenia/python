def metodoGet(url, user, senha):
    # Será utilizado somente para as Planilhas de Incidentes

    response = requests.request(
        'GET', url, verify=False, auth=HTTPBasicAuth(user, senha))
    conteudoMember = response.json()['member']
    for j in range(len(conteudoMember)):
        member = conteudoMember[j]
        if (member['status'] == "EMAND"):
            member['status'] = "Em Andamento"
        return conteudoMember


def dfInc(conteudoMember):
    df = pd.DataFrame(conteudoMember)
    df = pd.concat([df['ticketid'], df['descrpition'],
                   df['status'], df['internalpriority']], axis=1)
    df = df.reindex(columns=['tickedid', 'description',
                    'status', 'internalpriority'])
    df.columns = ['ID', 'Título', 'Status', 'Prioridade Interna']
    return df
