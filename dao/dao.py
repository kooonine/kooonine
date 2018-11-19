from iconservice import *


class daos(IconScoreBase):

    _LIST = 'list'
    _USER = 'user'
    _VOTE = 'vote'
    _USERNUM = 'usernum'
    _LIST_INFORMATION = 'list_information'

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._usernum = VarDB(self._USERNUM, db, value_type=int)
        self._user = DictDB(self._USER, db, value_type=int)
        self._vote = DictDB(self._VOTE, db, value_type=int, depth=2)
        self._list = ArrayDB(self._LIST, db, value_type=str)
        self._list_information = DictDB(self._LIST_INFORMATION, db, value_type=str)

    def on_install(self,test: str = None) -> None:
        super().on_install()
        self._usernum.set(1)
        self._user[self.owner] = self.now()

    def on_update(self) -> None:
        super().on_update()

    def user_is(self):
        if self._user[self.msg.sender]:
            return True
        return False

    def check_authority(self,code):
        if self._user[self.msg.sender] < int(json_loads(self._list_information[code])['date'])\
                and self._vote[self.msg.sender][code] == 0 \
                and json_loads(self._list_information[code])['result'] == "":
            return True
        return False

    def proposal(self,code,contents):
        code = code + str(len(self._list))
        self._list.put(code)
        self._list_information[code] = \
            f'{{"contents":"{contents}","date":"{self.now()}",' \
            f'"total_num":"{self._usernum.get()}",' \
            f'"agree_num":"{int(self._usernum.get() / 2 + 1)}",' \
            f'"opposition_num":"{int(self._usernum.get() / 2)}",' \
            f'"proposer":"{self.msg.sender}",' \
            f'"result":""}}'

    def excute(self,code,res):
        result = json_loads(self._list_information[code])
        if res == 1:
            result['agree_num'] = int(result['agree_num']) - 1
            if result['agree_num'] == 0:
                if code[:1] == 'A':
                    self._user[Address.from_string(result['contents'])] = self.now()
                    self._usernum.set(int(self._usernum.get()) + 1)
                elif code[:1] == 'R':
                    self._user[Address.from_string(result['contents'])] = ""
                    self._usernum.set(self._usernum.get() - 1)
                result['result'] = 'Allow'
                self._list_information[code] = json_dumps(result)
            else:
                self._list_information[code] = json_dumps(result)
        elif res == 2:
            result['opposition_num'] = int(result['opposition_num']) - 1
            if result['opposition_num'] <= 0:
                result['result'] = 'Refuse'
                self._list_information[code] = json_dumps(result)
            else:
                self._list_information[code] = json_dumps(result)

    @external
    def add_user(self, contents: Address):
        if self.user_is():
            if self._user[contents]:
                self.revert("existing user")
            self.proposal('A', contents)
        else:
            self.revert("not user")
        return True

    @external
    def remove_user(self, contents: Address):
        if self.user_is():
            if not self._user[contents]:
                self.revert("not existing user")
            self.proposal('R', contents)
        else:
            self.revert("not user")
        return True

    @external
    def ox(self, contents: str):
        if self.user_is():
            self.proposal('O', contents)
        else:
            self.revert("not user")
        return True

    @external
    def vote(self, code: str, vote_res: int):
        if self.user_is():
            if not vote_res == 1 or vote_res == 2:
                self.revert("not vote")
            if not self._list_information[code]:
                self.revert("not list_information")
            if self.check_authority(code):
                self._vote[self.msg.sender][code] = vote_res
                self.excute(code,vote_res)
            else:
                self.revert("not check_authority")
        else:
            self.revert("not user")
        return True

    @external
    def vote_list(self):
        if self.user_is():
            arr = []
            for e in self._list:
                arr.append('CODE : ' + e + ' info : ' + self._list_information[e] +
                           ' vote check : ' + str(self._vote[self.msg.sender][e]))
            return arr
        return 'not user'

    @external
    def vote_list_delete(self,code: str):
        if self.user_is():
            result = json_loads(self._list_information[code])
            if result['result'] == "" \
                    and Address.from_string(result['proposer']) == self.msg.sender:
                result['result'] = 'Delete'
                self._list_information[code] = json_dumps(result)
        else:
            self.revert("delete fail")
        return True
