# This function takes a set and spits out normal and prime form!
import numpy as np
def greatestDifference(pitches):
    max = np.NINF
    m_ind = -1
    s_set = pitches  # sorted in outer function
    for i in range(len(s_set) -1):
        if (s_set[i + 1] - s_set[i]) % 12 > max:
            max = (s_set[i + 1] - s_set[i]) % 12
            m_ind = i + 1
    if (s_set[0] - s_set[-1]) % 12 > max:
        m_ind = i + 1
    return m_ind


def primeForm(pitch_set):

    pitch_set.sort()
    subtrahend = pitch_set[greatestDifference(pitch_set)]
    temp = [(x - subtrahend) % 12 for x in pitch_set]
    temp.sort()
    mirrored = [(12 - y) % 12 for y in temp]
    mirrored.sort()
    temp_mirror = [(z - mirrored[greatestDifference(mirrored)]) % 12 for z in mirrored]
    temp_mirror.sort()
    if pitch_set == mirrored:
        return pitch_set
    if temp == temp_mirror:
        return temp
    else:
        for t, m in zip(temp, temp_mirror):
            if t == m:
                continue
            elif t < m:
                return temp
            else:
                return temp_mirror



if __name__ == "__main__":
    pitch_set = [1,7,8,3,11,9]
    print(primeForm(pitch_set))
