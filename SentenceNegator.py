import re
class SentenceNegator:
  IRREGULAR_ES_VERB_ENDINGS = ["ss", "x", "ch", "sh", "o"]

  def negate(self, sentence):
    # is
    if sentence.find("isn't") > -1:
      return sentence.replace("isn't", "is")

    if sentence.find("isn\\'t") > -1:
      return sentence.replace("isn\\'t", "is")

    if sentence.find("is not ") > -1:
      return sentence.replace("is not ", "is ")

    if sentence.find("is ") > -1:
      return sentence.replace("is ", "is not ")

    # has
    if sentence.find("does not have") > -1:
      return sentence.replace("does not have", "has")

    if sentence.find("doesn't have") > -1:
      return sentence.replace("doesn't have", "has")

    if sentence.find("doesn\\'t have") > -1:
      return sentence.replace("doesn\\'t have", "has")

    if sentence.find("has ") > -1:
      return sentence.replace("has ", "does not have ")

    # should
    if sentence.find("shouldn't") > -1:
      return sentence.replace("shouldn't", "should")

    if sentence.find("shouldn\\'t") > -1:
      return sentence.replace("shouldn\\'t", "should")

    if sentence.find("should not") > -1:
      return sentence.replace("should not", "should")

    if sentence.find("should") > -1:
      return sentence.replace("should", "should not")

    # must
    if sentence.find("mustn't") > -1:
      return sentence.replace("mustn't", "must")

    if sentence.find("mustn\\'t") > -1:
      return sentence.replace("mustn\\'t", "must")

    if sentence.find("must not") > -1:
      return sentence.replace("must not", "must")

    if sentence.find("must ") > -1:
      return sentence.replace("must ", "must not ")

    # can
    if sentence.find("can't") > -1:
      return sentence.replace("can't", "can")

    if sentence.find("can\\'t") > -1:
      return sentence.replace("can\\'t", "can")

    if sentence.find("cannot") > -1:
      return sentence.replace("cannot", "can")

    if sentence.find("can ") > -1:
      return sentence.replace("can ", "cannot ")
    # was
    if sentence.find(" was ") > -1:
      return sentence.replace(" was ", " was not ")
    if sentence.find("was not ") > -1:
      return sentence.replace("was not ", "was ")
    if sentence.find("wasn't") > -1:
      return sentence.replace("wasn't", "was")
    # doesn't work -> works
    doesnt_regex = r'(doesn\'t|doesn\\\'t|does not) (?P<verb>\w+)'

    if re.search(doesnt_regex, sentence):
      def replace_doesnt(matchobj):
        verb = matchobj.group(2)

        if verb.endswith("y") and self.__is_consonant(verb[-2]):
          return "{0}ies".format(verb[0:-1])

        for ending in self.IRREGULAR_ES_VERB_ENDINGS:
          if verb.endswith(ending):
            return "{0}es".format(verb)

        return "{0}s".format(verb)

      return re.sub(doesnt_regex, replace_doesnt, sentence, 1)

    verb_regex = r'(It |it |)(?P<verb>\w+)s( |$)'

    # works -> does not work
    def replace_verb(matchobj):
      subject = matchobj.group(1)
      verb = matchobj.group(2)
      whitespace = matchobj.group(3)

      # flies -> fly, but not die -> dy
      if verb.endswith("ie") and len(verb) > 3:
        verb = "{0}y".format(verb[0:-2])

      # stresses -> stress
      for ending in self.IRREGULAR_ES_VERB_ENDINGS:
        if verb.endswith("{0}e".format(ending)):
          verb = verb[0:-1]

      return "{0}does not {1}{2}".format(subject, verb, whitespace)

    if re.search(verb_regex, sentence):
      return re.sub(verb_regex, replace_verb, sentence, 1)

    return sentence

  def __is_consonant(self, letter):
    return letter not in ['a', 'e', 'i', 'o', 'u', 'y']
